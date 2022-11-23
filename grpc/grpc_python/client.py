from timeit import default_timer as timer
import grpc
import grpc_test_pb2
import grpc_test_pb2_grpc

start = timer()

channel = grpc.insecure_channel('localhost:50051')
stub = grpc_test_pb2_grpc.TestServiceStub(channel)

request = grpc_test_pb2.Data(value="Hello, World!")
response = stub.test_function(request)

end = timer()
print(end-start)


