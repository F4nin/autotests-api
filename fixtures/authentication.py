from clients.authentication.authentication_client import get_authentication_client, AuthenticationClient
import pytest

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
