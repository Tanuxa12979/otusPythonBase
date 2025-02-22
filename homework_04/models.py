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

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
import config

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


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        nullable=False,
    )

    username: Mapped[str] = mapped_column(
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


