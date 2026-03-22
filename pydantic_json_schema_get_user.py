from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema
# Добавили импорт функции validate_json_schema
from tools.assertions.schema import validate_json_schema
from tools.fakers import get_random_email
from clients.private_http_builder import AuthenticationUserSchema

# 1. Создаем публичного пользователя
public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)
create_user_response = public_users_client.create_user(create_user_request)

# 2. Создаём объект аутентификации для приватных запросов
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

# 3. Получаем приватного клиента с аутентификацией
private_users_client = get_private_users_client(authentication_user)

# 4. Выполняем запрос на получение данных о созданном пользователе
get_user_response = private_users_client.get_user_api(create_user_response.user.id)

# 5. Получаем JSON-схему из Pydantic-модели ответа
get_user_response_schema = GetUserResponseSchema.model_json_schema()

# 6. Валидируем ответ
validate_json_schema(instance=get_user_response.json(), schema=get_user_response_schema)

#Вывод
print("Валидация JSON-schema успешно пройдена!")
# print(get_user_response_schema)
# print(get_user_response.json())
#print(get_user_response.json())
print(f"User ID: {create_user_response.user.id}")
print(f"User email: {create_user_response.user.email}")








