from fastapi import APIRouter, HTTPException, Depends, Request
from sqlalchemy.orm import Session
from homework_04.models.user import User
from homework_04.schemas.user import UserCreate, UserRead  # Импортируем схемы
from homework_04.database import SessionLocal, engine
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


# Создаем таблицы в базе данных, если они еще не созданы
User.__table__.create(bind=engine, checkfirst=True)

router = APIRouter()
templates = Jinja2Templates(directory="templates")


# Зависимость для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Эндпоинт для получения пользователя по имени пользователя
@router.get("/{username}", response_model=UserRead)
def get_user(username: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# Эндпоинт для создания нового пользователя
@router.post("/", response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    new_user = User(name=user.name, username=user.username, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/show_users/", response_class=HTMLResponse)
def show_users(request: Request, db: Session = Depends(get_db)):
    users = db.query(User).all()
    return templates.TemplateResponse("show_users.html", {"request": request, "users": users})






