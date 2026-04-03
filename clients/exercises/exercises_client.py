from clients.api_client import APIClient
from httpx import Response
from clients.exercises.exercises_schema import ExerciseSchema, GetExercisesRequestSchema, CreateExerciseRequestSchema, \
    UpdateExerciseRequestSchema, GetExerciseResponseSchema, GetExercisesResponseSchema, CreateExerciseResponseSchema, \
    UpdateExerciseResponseSchema

from clients.private_http_builder import  get_private_http_client, AuthenticationUserSchema
import allure

from tools.routes import APIRoutes


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    @allure.step("Get exercises list")
    def get_exercises_api(self, request: GetExercisesRequestSchema) -> Response:
        """
        Метод получения списка курсов.

        :param request: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"{APIRoutes.EXERCISES}", params=request.model_dump(by_alias=True))

    @allure.step("Get exercises list by id {exercise_id}")
    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения упражнения.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"{APIRoutes.EXERCISES}/{exercise_id}")

    @allure.step("Create exercise")
    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Метод создания упражнения.

        :param request: Словарь с
        title, maxScore, minScore, courseId, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(f"{APIRoutes.EXERCISES}", json=request.model_dump(by_alias=True))

    @allure.step("Update exercise by id {exercise_id}")
    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        """
        Метод обновления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :param request: Словарь с title, maxScore, orderIndex, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request.model_dump(by_alias=True))

    @allure.step("Delete exercise by id {exercise_id}")
    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"{APIRoutes.EXERCISES}/{exercise_id}")

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        """
        Метод получения упражнения по exercise_id (ID).

        :param exercise_id: Идентификатор упражнения
        :return: Данные упражнения в виде словаря
        """
        response = self.get_exercise_api(exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def get_exercises(self, query: GetExercisesRequestSchema) -> GetExercisesResponseSchema:
        """
         Метод получение списка упражнений для курса.

         :param query: Параметры запроса (courseId)
         :return: Список упражнений в виде словаря
         """
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        """
        Метод создания нового упражнения.

        :param request: Данные для создания упражнения
        :return: Созданное упражнение в виде словаря
        """
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> UpdateExerciseResponseSchema:
        """
        Метод обновления существующего упражнения.

        :param exercise_id: Идентификатор упражнения
        :param request: Данные для обновления (только изменяемые поля)
        :return: Обновленное упражнение в виде словаря
        """
        response = self.update_exercise_api(exercise_id, request)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)

    def delete_exercise(self, exercise_id: str) -> str:
        response = self.delete_exercise_api(exercise_id)
        return response.text

def get_exercise_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))



