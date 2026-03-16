from httpx import Client

login_payload = {
  "email": "alexeyT@example.com",
  "password": "qwe123QWE"
}
base_url = 'http://localhost:8000/api/v1'


with Client() as client_for_login:
    login_response = client_for_login.post(f'{base_url}/authentication/login', json=login_payload)
    login_response_data = login_response.json()

    print("Status code:", login_response.status_code)
    print("Login response:", login_response_data)


    access_token = login_response_data['token']['accessToken']

headers = {f'Authorization': f'Bearer {access_token}'}
with Client(headers=headers) as auth_client:
    get_user_me_response = auth_client.get(f'{base_url}/users/me')
    print("Status code:", get_user_me_response.status_code)
    print(get_user_me_response.json())