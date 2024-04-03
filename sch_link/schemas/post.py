from typing import Optional

from pydantic import Field

from .base import Schema


class PostCreateForm(Schema):
    heading: str = Field(
        default=...,
        title="heading post",
        examples=["Post name"],
    )
    text: str = Field(
        default=...,
        title="Post text",
        examples=["Would you like ask me how i buy bitcoin?"],
    )
    picture: Optional[str] = Field(
        title="link from picture",
        examples=["https://i.imgur.com/HQ2RBhf.png"]
    )
    private: bool = Field(
        default=False,
        title="post private flag"
    )


class CommentPostCreate(Schema):
    text: str = Field(
        min_length=2,
        max_length=512
    )