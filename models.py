from pydantic import BaseModel


class Rules(BaseModel):
    rule: str
    value: int


class PasswordRules(BaseModel):
    password: str
    rules: list[Rules] | None = None


class PasswordVerification(BaseModel):
    verify: bool
    noMatch: list[str]
