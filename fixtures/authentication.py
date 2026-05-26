from pydantic import BaseModel

from clients.authentication.authentication_client import get_authentication_client, AuthenticationClient
import pytest

from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from fixtures.users import UserFixture


class AuthenticationFixture(BaseModel):
    """
    Фикстура, объединяющая запрос и ответ при аутентификации пользователя.

    Содержит данные запроса на логин и ответ сервера с токенами.
    Позволяет удобно получать токены для дальнейшего использования в тестах.

    Attributes:
        request: Данные запроса на аутентификацию (email, password)
        response: Ответ сервера с токенами авторизации
    """

    request: LoginRequestSchema
    response: LoginResponseSchema

    @property
    def refresh_token(self) -> str:
        return self.response.token.refresh_token

@pytest.fixture
def function_authentication(function_user: UserFixture, authentication_client: AuthenticationClient) -> AuthenticationFixture:
    """
    Фикстура, выполняющая аутентификацию созданного пользователя.

    Зависит от function_user, поэтому сначала создаётся пользователь,
    затем выполняется его вход в систему и возвращаются токены авторизации.

    Args:
        function_user: Фикстура с данными созданного пользователя
        authentication_client: Клиент для работы с эндпоинтами аутентификации

    Returns:
        AuthenticationFixture: Объект с данными запроса и ответа аутентификации
    """
    request = LoginRequestSchema(email=function_user.email, password=function_user.password)
    response = authentication_client.login(request=request)
    return AuthenticationFixture(
        request=request,
        response=response
    )

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
