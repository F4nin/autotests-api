from pydantic import BaseModel, Field, ConfigDict

from tools.fakers import fake


class TokenSchema(BaseModel):
    """
    Описание структуры аутентификационных токенов
    """
    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias='accessToken')
    refresh_token: str = Field(alias='refreshToken')


class LoginRequestSchema(BaseModel):
    """
    Описание структуры запроса на аутентификацию.
    """
    email: str = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)


class LoginResponseSchema(BaseModel):  # Добавили структуру ответа аутентификации
    """
    Описание структуры ответа аутентификации.
    """
    token: TokenSchema


class RefreshRequestSchema(BaseModel):
    """
    Описание структуры запроса для обновления токена.
    """
    model_config = ConfigDict(populate_by_name=True)

    refresh_token: str = Field(alias='refreshToken', default_factory=fake.sentence)  # Название ключа совпадает с API

class RefreshResponseSchema(BaseModel):
    """
    Описание структуры ответа обновления токена.
    """
    token: TokenSchema
