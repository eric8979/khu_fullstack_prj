import grpc
from concurrent import futures
import grpc_test_pb2
import grpc_test_pb2_grpc

class PythonServicer(grpc_test_pb2_grpc.TestServiceServicer):
    def test_function(self, request, context):
        response = grpc_test_pb2.Data() 
        response.value = request.value
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpc_test_pb2_grpc.add_TestServiceServicer_to_server(PythonServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()