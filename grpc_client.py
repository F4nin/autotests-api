import grpc
import user_service_pb2
import user_service_pb2_grpc


'''Создаем подключение к каналу'''
channel = grpc.insecure_channel('localhost:50051')

'''Инициализируем заглушку UserServiceStub используя channel'''
stub = user_service_pb2_grpc.UserServiceStub(channel)


response = stub.GetUser(user_service_pb2.GetUserRequest(username="test"))
print(response)
