from clients.exercises.exercises_client import get_exercise_client, ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from fixtures.courses import CourseFixture
from fixtures.users import UserFixture
import pytest
from pydantic import BaseModel

class ExerciseFixture(BaseModel):
    """
    Фикстура, объединяющая запрос и ответ при создании упражнения.

    Содержит данные запроса на создание упражнения (ID курса и т. д.) и ответ от сервера.
    Позволяет удобно работать с данными о созданном упражнении в тестах — получать ID,
    проверять метаданные и использовать их в последующих операциях.

    Attributes:
        request (CreateExerciseRequestSchema): Данные запроса на создание упражнения
        response (CreateExerciseResponseSchema): Ответ сервера с данными созданного упражнения
    """
    request: CreateExerciseRequestSchema
    response: CreateExerciseResponseSchema


@pytest.fixture
def exercises_client(function_user:UserFixture) -> ExercisesClient :
    """
    Фикстура для клиента работы с упражнениями с аутентификацией.

    Создаёт аутентифицированный клиент для взаимодействия с эндпоинтами API упражнений.
    Использует данные пользователя из фикстуры function_user для аутентификации в системе.

    Последовательность действий:
    1. Получение данных пользователя через фикстуру function_user.
    2. Выполнение аутентификации и получение JWT‑токена.
    3. Создание клиента ExercisesClient с установленным токеном.

    Args:
        function_user (UserFixture): Фикстура с данными созданного пользователя,
            необходимая для аутентификации при обращении к API

    Returns:
        ExercisesClient: Аутентифицированный клиент для работы с эндпоинтами упражнений
    """
    return get_exercise_client(function_user.authentication_user)

@pytest.fixture
def function_exercise(exercises_client: ExercisesClient,
                      function_course: CourseFixture
                      ) -> ExerciseFixture:
    """
    Фикстура, создающая тестовое упражнение.

    Автоматически создаёт новое упражнение, привязанное к существующему курсу,
    перед выполнением каждого теста, который запрашивает эту фикстуру.

    Процесс создания:
    1. Извлекается ID курса из фикстуры function_course.
    2. Формируется запрос CreateExerciseRequestSchema с указанием course_id.
    3. Через exercises_client отправляется запрос на создание упражнения.
    4. Сохраняются данные запроса и ответа в объект ExerciseFixture.

    Требования:
    - Предварительно должен быть создан курс (через фикстуру function_course).
    - Должен быть доступен аутентифицированный клиент exercises_client.

    Args:
        exercises_client (ExercisesClient): Аутентифицированный клиент для работы
            с эндпоинтами упражнений, используемый для отправки запроса на создание
        function_course (CourseFixture): Фикстура с данными созданного курса,
            из которой извлекается ID для привязки упражнения

    Returns:
        ExerciseFixture: Объект с данными запроса и ответа созданного упражнения.
            Может использоваться в тестах для:
            - Проверки корректности создания упражнения
            - Получения ID упражнения для последующих операций
            - Верификации метаданных упражнения из ответа сервера
    """
    request = CreateExerciseRequestSchema(course_id=function_course.response.course.id)
    response = exercises_client.create_exercise(request)
    return ExerciseFixture(request=request, response=response)
