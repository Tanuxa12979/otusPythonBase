from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from homework_04.models.user import User
from homework_04.schemas.user import UserCreate, UserResponse  # Импортируем схемы
from homework_04.database import SessionLocal, engine

# Создаем таблицы в базе данных, если они еще не созданы
User.__table__.create(bind=engine, checkfirst=True)

router = APIRouter()


# Зависимость для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Эндпоинт для получения пользователя по имени пользователя
@router.get("/{username}", response_model=UserResponse)
async def get_user(username: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# Эндпоинт для создания нового пользователя
@router.post("/", response_model=UserResponse)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    new_user = User(name=user.name, username=user.username, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user