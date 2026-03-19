import uuid
from typing import Annotated

from pydantic import BaseModel, Field, EmailStr, StringConstraints

String250 = Annotated[str, StringConstraints(min_length=1, max_length=250)]
String50 = Annotated[str, StringConstraints(min_length=1, max_length=50)]

class CreateUserRequestSchema(BaseModel):
    """
    Запрос на создание пользователя
    """
    email: EmailStr
    password: String250
    last_name: String50 = Field(alias="lastName")
    first_name: String50 = Field(alias="firstName")
    middle_name: String50 = Field(alias="middleName")

class UserSchema(BaseModel):
    """
    Модель данных пользователя
    (User)
    """
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    email: EmailStr
    last_name: String50 = Field(alias="lastName")
    first_name: String50 = Field(alias="firstName")
    middle_name: String50 = Field(alias="middleName")

class CreateUserResponseSchema(BaseModel):
    """
    Ответ с данными созданного пользователя
    """
    user: UserSchema

