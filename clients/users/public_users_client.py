from httpx import Response

from clients.api_client import APIClient
from typing import TypedDict

class CreateUserRequest(TypedDict):
    """
    Описание структуры запроса для создания пользователя
    """
    email: str
    password: str
    lastName: str   # Название ключа совпадает с API
    firstName: str  # Название ключа совпадает с API
    middleName: str # Название ключа совпадает с API

class PublicUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """
    def create_user_api(self, request: CreateUserRequest) -> Response:
        """
        Публичный метод для создания пользователя
        :param request: словарь со структурой CreateUserRequest
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users",json=request)