from pydantic import BaseModel

from clients.files.files_client import get_files_client, FilesClient
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
import pytest

from config import settings
from fixtures.users import UserFixture

class FileFixture(BaseModel):
    """
    Фикстура, объединяющая запрос и ответ при создании файла.

    Содержит как данные запроса на создание файла (путь к файлу и т. д.), так и ответ от сервера.
    Позволяет удобно работать с данными о созданном файле в тестах.

    Attributes:
        request (CreateFileRequestSchema): Данные запроса на создание файла
        response (CreateFileResponseSchema): Ответ сервера с данными созданного файла
    """
    request: CreateFileRequestSchema
    response: CreateFileResponseSchema

@pytest.fixture
def files_client(function_user: UserFixture) -> FilesClient:
    """
    Фикстура для клиента работы с файлами с аутентификацией.

    Создаёт аутентифицированный клиент для работы с эндпоинтами API файлов.
    Использует данные пользователя из фикстуры function_user для аутентификации.

    Фикстура зависит от function_user, поэтому сначала будет выполнен вход пользователя
    в систему, затем создан клиент с установленным JWT‑токеном для всех последующих запросов.

    Args:
        function_user (UserFixture): Фикстура с данными созданного пользователя,
            используемая для аутентификации в API

    Returns:
        FilesClient: Аутентифицированный клиент для работы с эндпоинтами файлов
    """
    return get_files_client(function_user.authentication_user)

@pytest.fixture
def function_file(files_client: FilesClient) -> FileFixture:
    """
    Фикстура, создающая тестовый файл.

    Создаёт новый файл с предопределёнными данными (в данном случае — изображение PNG).
    Используется для подготовки тестовых данных перед выполнением тестов,
    которые требуют наличия загруженного файла.

    Перед каждым тестом, запрашивающим эту фикстуру, автоматически выполняется:
    1. Загрузка тестового файла (image.png) через files_client.
    2. Сохранение данных запроса и ответа в объект FileFixture.

    Args:
        files_client (FilesClient): Аутентифицированный клиент для работы
            с эндпоинтами файлов, используемый для отправки запроса на создание файла

    Returns:
        FileFixture: Объект с данными запроса и ответа созданного файла,
            который можно использовать в тестах для проверки свойств файла
            или передачи в другие операции API
    """
    request = CreateFileRequestSchema(upload_file=settings.test_data.image_png_file)
    response = files_client.create_file(request)
    return FileFixture(request=request, response=response)