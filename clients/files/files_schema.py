import uuid

from pydantic import BaseModel, HttpUrl, Field

class FileSchema(BaseModel):
    """
    Описание структуры файла.
    """
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    url: HttpUrl
    filename: str
    directory: str

class CreateFileRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание файла.
    """
    filename: str
    directory: str
    upload_file: str

class CreateFileResponseSchema(BaseModel):
    """
    Описание структуры ответа создания файла.
    """
    file: FileSchema