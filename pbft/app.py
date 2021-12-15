
from pbft.protos import message_pb2_grpc
from pbft.protos import message_pb2
from pbft.protos.message_pb2_grpc import SampleServiceServicer
import grpc
from concurrent import futures
import time
import sys

addr = ""
addrs = []

def sendTx(addr, tx):
  with grpc.insecure_channel(addr) as channel:
    stub = message_pb2_grpc.SampleServiceStub(channel)
    response = stub.Share(tx)
    return response

class SimpleService(SampleServiceServicer):

  def __init__(self):
    pass

  def Share(self, req, ctx): 

    if req.state == "req":
      print("I received and accept")
      # Task1 
      return message_pb2.ShareResp(text="accept")

    if req.state == "pre-prepare":
      print("I received prepare tx")
      # Task2
      return message_pb2.ShareResp(text="accept")

    if req.state == "prepare":
      print("I received prepare tx")
      # Task3
      return message_pb2.ShareResp(text="accept")

    if req.state == "commit":
      print("I received commit tx")
      # Task4
      pass

    return message_pb2.ShareResp(text="")

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  message_pb2_grpc.add_SampleServiceServicer_to_server(SimpleService(), server)
  server.add_insecure_port(addr)
  server.start()
  print('Starting gRPC server. on:{}'.format(addr))
  try:
    while True:
      time.sleep(3600)
  except KeyboardInterrupt:
    server.stop(0)

if __name__ == '__main__':
  addr = sys.argv[1]
  addrs = sys.argv[2].split(",")
  if len(sys.argv) >= 2:
    isEvil = sys.argv[2]
  print("addrs:{}".format(addrs))
  serve()
  