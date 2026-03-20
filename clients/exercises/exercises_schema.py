import uuid
from typing import Annotated

from pydantic import BaseModel, Field, ConfigDict, EmailStr, StringConstraints

String250 = Annotated[str, StringConstraints(min_length=1, max_length=250)]
String_more_1_simbols = Annotated[str, StringConstraints(min_length=1, max_length=50)]

class ExerciseSchema(BaseModel):
    """
    Описание структуры упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: String250
    course_id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="courseId")
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: String_more_1_simbols
    estimated_time: str | None = Field(alias="estimatedTime")

class UpdateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа обновления упражнения.
    """
    exercise: ExerciseSchema

class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа получения упражнений.
    """
    model_config = ConfigDict(populate_by_name=True)

    exercises: list[ExerciseSchema]

class GetExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа получения упражнения.
    """
    exercise: ExerciseSchema

class CreateExerciseResponseSchema(BaseModel):
    """
     Описание структуры ответа создания упражнения.
     """
    exercise: ExerciseSchema

class GetExercisesRequestSchema(BaseModel):
    """
    Описание структуры запроса на получение списка упражнений.
    """
    model_config = ConfigDict(populate_by_name=True)

    course_id: str = Field(alias="courseId")

class CreateExercisesRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: String250
    course_id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="courseId")
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: String_more_1_simbols
    estimated_time: str | None = Field(alias="estimatedTime")

class UpdateExercisesRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int | None = Field(alias="orderIndex")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")
