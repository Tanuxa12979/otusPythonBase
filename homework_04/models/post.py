from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped, declarative_base
from homework_04.database import Base


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