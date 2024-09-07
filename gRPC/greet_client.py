import greet_pb2_grpc
import greet_pb2

import grpc
import time

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = greet_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(greet_pb2.HelloRequest(name='you'))
    print("Greeter client received: " + response.message)

    response = stub.ParrotSaysHello(greet_pb2.HelloRequest(name='you'))
    for res in response:
        print("Greeter client received: " + res.message)

    response = stub.ChattyClientSaysHello(iter([greet_pb2.HelloRequest(name='you')]))
    for res in response:
        print("Greeter client received: " + res.message)


if __name__ == '__main__':
    run()
    while True:
        time.sleep(_ONE_DAY_IN_SECONDS)
