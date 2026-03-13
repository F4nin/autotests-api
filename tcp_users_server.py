import socket

message_history = []

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ("localhost", 12345)
    server_socket.bind(server_address)

    server_socket.listen(10)
    print("Сервер запущен и ждёт подключения...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Пользователь с адресом: {client_address} подключился к серверу")

        if message_history:
            history_str = '\n'.join(message_history)
            client_socket.send(history_str.encode())

        data = client_socket.recv(1024).decode()
        if not data:
            client_socket.close()
            continue

        print(f"Пользователь с адресом: {client_address} отправил сообщение: {data}")

        # Сохраняем в историю
        message_history.append(data)

        # Отправляем ответ
        response = f"Сервер получил: {data}"
        client_socket.send(response.encode())

        client_socket.close()

if __name__ == "__main__":
    server()