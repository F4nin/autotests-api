from pydantic import BaseModel
from clients.courses.courses_client import CoursesClient, get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema, CreateCourseResponseSchema
from fixtures.files import FileFixture
from fixtures.users import UserFixture
import pytest

class CourseFixture(BaseModel):
    """
    Фикстура, объединяющая запрос и ответ при создании курса.

    Содержит данные запроса на создание курса (ID превью‑файла, ID создателя и т. д.)
    и ответ от сервера. Позволяет удобно работать с данными о созданном курсе в тестах —
    получать ID, проверять метаданные, использовать их в последующих операциях.

    Attributes:
        request (CreateCourseRequestSchema): Данные запроса на создание курса
        response (CreateCourseResponseSchema): Ответ сервера с данными созданного курса
    """
    request: CreateCourseRequestSchema
    response: CreateCourseResponseSchema

@pytest.fixture
def courses_client(function_user: UserFixture) -> CoursesClient:
    """
    Фикстура для клиента работы с курсами с аутентификацией.

    Создаёт аутентифицированный клиент для взаимодействия с эндпоинтами API курсов.
    Использует данные пользователя из фикстуры function_user для аутентификации в системе.

    Последовательность действий:
    1. Получение данных пользователя через фикстуру function_user.
    2. Выполнение аутентификации и получение JWT‑токена.
    3. Создание клиента CoursesClient с установленным токеном для всех последующих запросов.

    Args:
        function_user (UserFixture): Фикстура с данными созданного пользователя,
            необходимая для аутентификации при обращении к API

    Returns:
        CoursesClient: Аутентифицированный клиент для работы с эндпоинтами курсов
    """
    return get_courses_client(function_user.authentication_user)

@pytest.fixture
def function_course(courses_client: CoursesClient,
                    function_user: UserFixture,
                    function_file: FileFixture
                    ) -> CourseFixture:
    """
    Фикстура, создающая тестовый курс.

    Автоматически создаёт новый курс с привязанным превью‑файлом перед выполнением каждого теста,
    который запрашивает эту фикстуру.

    Процесс создания:
    1. Извлекается ID файла из фикстуры function_file (используется как превью курса).
    2. Извлекается ID пользователя из фикстуры function_user (указывается как создатель курса).
    3. Формируется запрос CreateCourseRequestSchema с указанием preview_file_id и created_by_user_id.
    4. Через courses_client отправляется запрос на создание курса.
    5. Сохраняются данные запроса и ответа в объект CourseFixture.

    Требования:
    - Предварительно должен быть создан пользователь (через фикстуру function_user).
    - Предварительно должен быть загружен файл (через фикстуру function_file).
    - Должен быть доступен аутентифицированный клиент courses_client.

    Args:
        courses_client (CoursesClient): Аутентифицированный клиент для работы
            с эндпоинтами курсов, используемый для отправки запроса на создание
        function_user (UserFixture): Фикстура с данными созданного пользователя,
            из которой извлекается ID для указания создателя курса
        function_file (FileFixture): Фикстура с данными созданного файла,
            из которой извлекается ID для установки в качестве превью курса

    Returns:
        CourseFixture: Объект с данными запроса и ответа созданного курса.
            Может использоваться в тестах для:
            - Проверки корректности создания курса
            - Получения ID курса для последующих операций
            - Верификации метаданных курса из ответа сервера
            - Тестирования операций, требующих наличия курса (например, добавление упражнений)
    """
    request = CreateCourseRequestSchema(
        preview_file_id=function_file.response.file.id,
        created_by_user_id=function_user.response.user.id
    )
    response = courses_client.create_course(request)
    return CourseFixture(request=request, response=response)