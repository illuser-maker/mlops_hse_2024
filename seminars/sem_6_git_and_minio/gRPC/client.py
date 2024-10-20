import grpc
import test_grpc_pb2
import test_grpc_pb2_grpc


def run():
    print("Will try to greet world ...")
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = test_grpc_pb2_grpc.GreeterStub(channel)
        response = stub.PrintHelloWorld(test_grpc_pb2.HelloRequest(name='gleb'))
        print("Greeter client received: " + response.message + " with name " + response.name)

        response = stub.PrintAgain(test_grpc_pb2.HelloRequest(name='lol'))
        print("Greeter client received: " + response.message + " with name " + response.name)


if __name__ == '__main__':
    run()