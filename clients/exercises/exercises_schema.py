from typing import Annotated

from pydantic import BaseModel, Field, ConfigDict, EmailStr, StringConstraints
from tools.fakers import fake

String250 = Annotated[str, StringConstraints(min_length=1, max_length=250)]
String_more_1_simbols = Annotated[str, StringConstraints(min_length=1, max_length=50)]

class ExerciseSchema(BaseModel):
    """
    Описание структуры упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: String250
    course_id: str = Field(alias="courseId")
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

class CreateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: String250 = Field(default_factory=fake.sentence)
    course_id: str = Field(alias="courseId", default_factory=fake.uuid4)
    max_score: int | None = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int | None = Field(alias="minScore", default_factory=fake.min_score)
    order_index: int = Field(alias="orderIndex", default_factory=fake.integer)
    description: String_more_1_simbols = Field(default_factory=fake.text)
    estimated_time: str | None = Field(alias="estimatedTime", default_factory=fake.estimated_time)

class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None = Field(default_factory=fake.sentence)
    max_score: int | None = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int | None = Field(alias="minScore", default_factory=fake.min_score)
    order_index: int | None = Field(alias="orderIndex", default_factory=fake.integer)
    description: str | None = Field(default_factory=fake.text)
    estimated_time: str | None = Field(alias="estimatedTime", default_factory=fake.estimated_time)

class UpdateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа обновления упражнения.
    """
    exercise: ExerciseSchema