from typing import TYPE_CHECKING, Union
from datetime import datetime

from sqlalchemy import (Column,
                        BIGINT,
                        VARCHAR,
                        ForeignKey,
                        CheckConstraint,
                        CHAR,
                        BOOLEAN,
                        DATETIME,
                        )
from sqlalchemy.orm import relationship

from .base import Base


__all__ = [
    "Base",
    "User",
    "Post",
    "Comment"
]

class User(Base):
    __table_args__ = (
        CheckConstraint("length(email) >= 5"),
        CheckConstraint("length(name) <= 128"),
        CheckConstraint("email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z]{2,}$'"),
    )

    if TYPE_CHECKING:
        id: Union[int, Column]
        name: str
        email: str
        password: str
        comment: list["Comment"]
        date_registry: datetime
        post: list["Post"]
    else:
        id = Column(BIGINT, primary_key=True)
        name = Column(VARCHAR(length=128), nullable=False, unique=True)
        email = Column(VARCHAR(length=128), nullable=False, unique=True)
        password = Column(CHAR(length=64), nullable=False)
        date_registry = Column(DATETIME, default=datetime.now())
        comment = relationship(argument="Comment", back_populates="user")
        post = relationship("Post", back_populates="user")

    def __str__(self) -> str:
        return self.name


class Post(Base):
    if TYPE_CHECKING:
        id: Union[int, Column]
        id_user: int
        heading: str
        text: str
        date_create: datetime
        picture: str
        private: bool
    else:
        id = Column(BIGINT, primary_key=True)
        id_user = Column(
            ForeignKey(
                column=User.id,
                ondelete="CASCADE",
                onupdate="CASCADE",
            ),
            nullable=False,
            index=True
        )
        heading = Column(VARCHAR(length=128), nullable=False)
        text = Column(VARCHAR(length=1024), nullable=False)
        picture = Column(CHAR(64), nullable=True)
        date_create = Column(DATETIME, default=datetime.now())
        private = Column(BOOLEAN, nullable=False, default=False)
        user = relationship("User", back_populates="post")
        comment = relationship("Comment", back_populates="post")

    def __str__(self) -> str:
        return self.heading


class Comment(Base):
    __table_args__ = (
        CheckConstraint("length(text) >= 2"),
    )

    if TYPE_CHECKING:
        id: int
        id_user: int
        id_post: int
        date_create: datetime
        text: str
    else:
        id = Column(BIGINT, primary_key=True)
        date_create = Column(DATETIME, default=datetime.now())
        id_user = Column(
            ForeignKey(
                column=User.id,
                ondelete="CASCADE",
                onupdate="CASCADE",
            ),
            nullable=False,
            index=True,
        )
        id_post = Column(
            ForeignKey(
                column=Post.id,
                ondelete="CASCADE",
                onupdate="CASCADE",
            ),
            nullable=False,
            index=True,
        )
        text = Column(VARCHAR(length=512), nullable=False)
        user = relationship("User", back_populates="comment")
        post = relationship("Post", back_populates="comment")
