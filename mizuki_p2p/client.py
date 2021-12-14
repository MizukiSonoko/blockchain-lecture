
from p2p.protos import message_pb2_grpc
from p2p.protos import message_pb2
import grpc

with grpc.insecure_channel("localhost:50051") as channel:
  stub = message_pb2_grpc.SampleServiceStub(channel)
  response = stub.PingPong(
    message_pb2.Ping(
      text="ping",
      count=0,
      addr="localhost:50052"
    ))
  print(response)