from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, mapped_column, Mapped
from homework_04.database import Base


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