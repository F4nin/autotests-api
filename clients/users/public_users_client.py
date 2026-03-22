from httpx import Response

from clients.api_client import APIClient
from clients.users.users_schema import CreateUserResponseSchema, CreateUserRequestSchema

from clients.public_http_builder import get_public_http_client


class PublicUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """
    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        Публичный метод для создания пользователя
        :param request: словарь со структурой CreateUserRequestSchema
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users",json=request.model_dump(by_alias=True))

    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        response =self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)

def get_public_users_client() -> PublicUsersClient:
    return PublicUsersClient(client=get_public_http_client())