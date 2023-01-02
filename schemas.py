from pydantic import BaseModel
from typing import Literal


class Rules(BaseModel):
    rule: Literal[
        "minSize",
        "minUppercase",
        "minLowercase",
        "minDigit",
        "minSpecialChars",
    ]
    value: int


class PasswordRules(BaseModel):
    password: str
    rules: list[Rules] | None = None


class PasswordVerification(BaseModel):
    verify: bool
    noMatch: list[str]
