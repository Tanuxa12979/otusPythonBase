from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from homework_04.config import db_url

# Создание движка базы данных
engine = create_engine(db_url)

# Создание класса для сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Создание базового класса для моделей
Base = declarative_base()







