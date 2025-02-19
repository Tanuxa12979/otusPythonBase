from sqlalchemy import Column, Integer, String, Text, text
import asyncio
from sqlalchemy.orm import Mapped, sessionmaker
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

import config

#PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"

engine = create_async_engine(
    config.db_async_url,
    # echo=True only for debug!!
    echo=config.db_echo,
    pool_size=config.db_pool_size,
    max_overflow=config.db_max_overflow,
)


async_session_factory = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
)


Base = declarative_base()
#Session = None


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        nullable=False,
    )

    surname: Mapped[str] = mapped_column(
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        nullable=False,
        unique=True,
    )

    posts = relationship("Post", back_populates="user")

class Post(Base):
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    title: Mapped[str] = mapped_column(
        nullable=False,
    )

    body: Mapped[str] = mapped_column(
        nullable=False,
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id'),
        nullable=False
    )

    user = relationship("User", back_populates="posts")


# async def main():
#     async with async_session_factory() as session:
#         async with session.begin():
#             result = await session.execute(text("SELECT 'hello world'"))
#             print(result.all())
#
# # Запуск асинхронной функции
# if __name__ == "__main__":
#     asyncio.get_event_loop().run_until_complete(main())

