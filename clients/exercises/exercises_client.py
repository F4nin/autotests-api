from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

from clients.private_http_builder import  get_private_http_client, AuthenticationUserSchema


class Exercise(TypedDict):
    """
    Описание структуры упражнения.
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class UpdateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа обновления упражнения.
    """
    exercise: Exercise

class GetExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа получения упражнений.
    """
    exercises: list[Exercise]

class GetExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа получения упражнения.
    """
    exercise: Exercise

class CreateExerciseResponseDict(TypedDict):
    """
     Описание структуры ответа создания упражнения.
     """
    exercise: Exercise

class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка упражнений.
    """
    courseId: str

class CreateExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на создание упражнения.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class UpdateExercisesRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление упражнения.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """
    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод получения списка курсов.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения упражнения.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExercisesQueryDict) -> Response:
        """
        Метод создания упражнения.

        :param request: Словарь с
        title, maxScore, minScore, courseId, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExercisesRequestDict) -> Response:
        """
        Метод обновления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :param request: Словарь с title, maxScore, orderIndex, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        """
        Метод получения упражнения по exercise_id (ID).

        :param exercise_id: Идентификатор упражнения
        :return: Данные упражнения в виде словаря
        """
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        """
         Метод получение списка упражнений для курса.

         :param query: Параметры запроса (courseId)
         :return: Список упражнений в виде словаря
         """
        response = self.get_exercises_api(query)
        return response.json()

    def create_exercise(self, request: CreateExercisesQueryDict) -> CreateExerciseResponseDict:
        """
        Метод создания нового упражнения.

        :param request: Данные для создания упражнения
        :return: Созданное упражнение в виде словаря
        """
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercise(self, exercise_id: str, request: UpdateExercisesRequestDict) -> UpdateExerciseResponseDict:
        """
        Метод обновления существующего упражнения.

        :param exercise_id: Идентификатор упражнения
        :param request: Данные для обновления (только изменяемые поля)
        :return: Обновленное упражнение в виде словаря
        """
        response = self.update_exercise_api(exercise_id, request)
        return response.json()

    def delete_exercise(self, exercise_id: str) -> str:
        response = self.delete_exercise_api(exercise_id)
        return response.text

def get_exercise_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))



