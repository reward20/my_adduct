from .base import Schema
from .check_types import PasswordStr
from pydantic import Field, EmailStr, model_validator
from typing import Self, Optional


class RegisterForm(Schema):
    email: EmailStr = Field(
        default=...,
        title="User email",
        examples=["karden@gmail.com"]
    )
    password: PasswordStr = Field(
        default=...,
        title="Password",
        examples=["cHeckMyPasswword1o1"]
    )
    confirm_password: PasswordStr = Field(
        default=...,
        title="Confirm Password",
        examples=["VeryStrongPassword1!"]
    )

    @model_validator(mode="after")
    def validator(self) -> Self:
        if self.password != self.confirm_password:
            raise ValueError("the password and the confirm_password do not match")

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
    pass


class CommentForm(Schema):
    pass