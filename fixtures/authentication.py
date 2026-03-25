from clients.authentication.authentication_client import get_authentication_client, AuthenticationClient
import pytest
from pydantic import BaseModel, EmailStr

from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import PrivateUsersClient, get_private_users_client
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema

@pytest.fixture
def authentication_client() -> AuthenticationClient:
    """
    Фикстура для клиента аутентификации.

    Предоставляет клиент для работы с эндпоинтами аутентификации:
    - Логин пользователя
    - Получение токенов

    Returns:
       AuthenticationClient: Клиент для аутентификации
    """
    return get_authentication_client()
