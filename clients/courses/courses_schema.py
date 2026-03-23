import uuid
from typing import Annotated

from pydantic import BaseModel, Field, ConfigDict, EmailStr, StringConstraints

from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema
from tools.fakers import fake

String250 = Annotated[str, StringConstraints(min_length=1, max_length=250)]
String_more_1_simbols = Annotated[str, StringConstraints(min_length=1, max_length=50)]

class CourseSchema(BaseModel):

    """
    Описание структуры курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: String250
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    description: String_more_1_simbols
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str | None = Field(alias="estimatedTime")
    created_by_user: UserSchema = Field(alias="createdByUser")

class CreateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания курса.
    """
    course: CourseSchema

class GetCoursesRequestSchema(BaseModel):
    """
    Описание структуры запроса на получение списка курсов.
    """
    model_config = ConfigDict(populate_by_name=True)
    user_id: str = Field(alias="userId")

class GetCourseResponseSchema(BaseModel):
    course: CourseSchema

class CreateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: String250 = Field(default_factory=fake.sentence)
    max_score: int | None = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int | None = Field(alias="minScore", default_factory=fake.min_score)
    description: String_more_1_simbols = Field(default_factory=fake.text)
    estimated_time: str | None = Field(alias="estimatedTime", default_factory=fake.estimated_time)
    preview_file_id: str = Field(alias="previewFileId", default_factory=fake.uuid4)
    created_by_user_id: str = Field(alias="createdByUserId", default_factory=fake.uuid4)

class UpdateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: String250 | None = Field(default_factory=fake.sentence)
    max_score: int | None = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int | None = Field(alias="minScore", default_factory=fake.min_score)
    description: str | None = Field(default_factory=fake.text)
    estimated_time:str | None = Field(alias="estimatedTime", default_factory=fake.estimated_time)
