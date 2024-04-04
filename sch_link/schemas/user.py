from .base import Schema
from .check_types import PasswordStr
from pydantic import Field, EmailStr, model_validator, HttpUrl, PositiveInt
from typing import Optional, Self

__all__ = [
    "RegisterForm",
    "LoginForm",
    "PostForm",
    "CommentForm",
    "UserDetail",
]


class RegisterForm(Schema):
    email: EmailStr = Field(
        default=...,
        title="User email",
        examples=["karden@gmail.com"]
    )
    password: PasswordStr = Field(
        default=...,
        title="Password",
        examples=["cHeckMyPa$swword1o1"]
    )
    confirm_password: PasswordStr = Field(
        default=...,
        title="Confirm Password",
        examples=["cHeckMyPa$swword1o1"]
    )

    @model_validator(mode="after")
    def validator(self) -> Self:
        if self.password != self.confirm_password:
            raise ValueError(
                "the password and the confirm_password do not match"
                )

        return self


class LoginForm(Schema):
    email: EmailStr = Field(
        default=...,
        title="User email",
        examples=["jone@doe.com"]
    )
    password: PasswordStr = Field(
        default=...,
        title="Password",
        examples=["cHeckMyPasswword1o1"]
    )


class PostForm(Schema):
    heading: str = Field(
        default=...,
        min_length=2,
        max_length=128,
    )
    text: str = Field(
        default=...,
        min_length=2,
        max_length=128,
    )
    picture: Optional[HttpUrl] = Field(
        default=None,
        title="Url to icon post"
    )
    private: bool = Field(
        default=False,
    )


class CommentForm(Schema):
    text: str = Field(
        default=...,
        min_length=2,
        max_length=512,
    )


class UserDetail(Schema):
    id: PositiveInt = Field(
        default=...,
        title="User ID",
        examples=[42]
    )
    email: EmailStr = Field(
        default=...,
        title="User email",
        examples=["jone@doe.com"]
    )
