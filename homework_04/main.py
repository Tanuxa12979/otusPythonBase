from fastapi import FastAPI
from homework_04.routers.user import router  # Импортируем маршруты пользователей
from database import engine, Base

# Создаем экземпляр FastAPI
app = FastAPI()

# Создаем все таблицы в базе данных (если они еще не созданы)
Base.metadata.create_all(bind=engine)

# Подключаем маршруты
app.include_router(router, prefix="/user", tags=["users"])

# Запуск приложения
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)



