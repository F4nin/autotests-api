from clients.authentication.authentication_client import get_authentication_client, AuthenticationClient
import pytest
from pydantic import BaseModel, EmailStr

from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import PrivateUsersClient, get_private_users_client
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema

class UserFixture(BaseModel):
    """
    Фикстура, объединяющая запрос и ответ при создании пользователя.

    Содержит как данные запроса (email, пароль и т.д.), так и ответ от сервера.
    Позволяет удобно получать email, пароль и данные для аутентификации.

    Attributes:
    request: Данные запроса на создание пользователя
    response: Ответ сервера с данными созданного пользователя
    """
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self) -> EmailStr:
        return self.request.email

    @property
    def password(self) -> str:
        return self.request.password

    @property
    def authentication_user(self) -> AuthenticationUserSchema:
        """
        Формирует модель для аутентификации, используя данные пользователя.
        """
        return AuthenticationUserSchema(email=self.request.email, password=self.request.password)

@pytest.fixture
def public_users_client() -> PublicUsersClient:
    """
    Фикстура для публичного клиента пользователей.

    Предоставляет клиент для работы с публичными эндпоинтами API:
    - Создание пользователя
    - Публичные методы, не требующие аутентификации

    Returns:
        PublicUsersClient: Публичный клиент для работы с пользователями
    """
    return get_public_users_client()

@pytest.fixture
def function_user(public_users_client: PublicUsersClient) -> UserFixture:
    """
    Фикстура, создающая тестового пользователя.

    Создает нового пользователя с случайными данными (email, пароль и т.д.)
    Использует генерацию через Faker.

    Фикстура автоматически создает пользователя перед каждым тестом,
    который ее запрашивает.

    Args:
        public_users_client: Фикстура публичного клиента для создания пользователя

    Returns:
        UserFixture: Объект с данными запроса и ответа созданного пользователя
    """
    request = CreateUserRequestSchema()
    response = public_users_client.create_user(request)
    return UserFixture(request=request, response=response)

@pytest.fixture
def private_users_client(function_user: UserFixture) -> PrivateUsersClient:
    """
    Фикстура для приватного клиента пользователей с аутентификацией.

    Создает аутентифицированный клиент, используя данные созданного пользователя.
    Выполняет логин и устанавливает JWT токен для всех последующих запросов.

    Фикстура зависит от function_user, поэтому сначала будет создан пользователь,
    затем выполнен его вход в систему, и только потом возвращен клиент.

    Args:
       function_user: Фикстура с данными созданного пользователя

    Returns:
       PrivateUsersClient: Аутентифицированный клиент для работы с приватными эндпоинтами
    """
    return get_private_users_client(function_user.authentication_user)
