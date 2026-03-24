from http import HTTPStatus

from clients.authentication.authentication import assert_login_response
from clients.users.public_users_client import get_public_users_client
from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.base import assert_status_code, assert_equal, assert_is_true
from tools.assertions.schema import validate_json_schema


def test_login():
    public_user_client = get_public_users_client()

    request_create_user = CreateUserRequestSchema()
    response_create_user = public_user_client.create_user_api(request_create_user)
    response_create_user_data = CreateUserResponseSchema.model_validate_json(response_create_user.text)

    authentication_client = get_authentication_client()

    request_login = LoginRequestSchema(email=response_create_user_data.user.email, password=request_create_user.password)
    response_login = authentication_client.login_api(request_login)
    response_login_data = LoginResponseSchema.model_validate_json(response_login.text)

    assert_status_code(response_login.status_code, HTTPStatus.OK)

    assert_login_response(response_login_data)

    validate_json_schema(response_login.json(), response_login_data.model_json_schema())