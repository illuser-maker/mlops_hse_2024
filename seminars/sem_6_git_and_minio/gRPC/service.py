import test_grpc_pb2
import test_grpc_pb2_grpc

class Greeter(test_grpc_pb2_grpc.GreeterServicer):
    def PrintAgain(self, request: test_grpc_pb2.HelloRequest, context):
        print(request)
        response = test_grpc_pb2.HelloResponse(name=request.name)
        print(response)
        response.message += 'lol kek чебурек'
        return response

    def PrintHelloWorld(self, request, context):
        print(request)
        return test_grpc_pb2.HelloResponse(name=request.name, message='lol')