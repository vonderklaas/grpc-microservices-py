from concurrent import futures
import logging

import grpc
import users_pb2
import users_pb2_grpc

class UsersServicer(users_pb2_grpc.UsersServicer):
    def GetUsers(self, request, context):
        return users_pb2.GetUsersResponse(users=[
            users_pb2.User(id="1", name="John Doe", email="john.doe@example.com", password="password"),
        ])


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    users_pb2_grpc.add_UsersServicer_to_server(UsersServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
