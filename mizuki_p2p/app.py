
from p2p.protos import message_pb2_grpc
from p2p.protos import message_pb2
from p2p.protos.message_pb2_grpc import SampleServiceServicer
import grpc
from concurrent import futures
import time
import sys

addr = ""

class SimpleService(SampleServiceServicer):

  def __init__(self):
    pass

  def Hello(self, req, ctx):
    # This is sample implements of Code. 
    print(req.ping) # Print ping text
    return message_pb2.SimpleResp(pong = "pong")

  def PingPong(self, req, ctx): 
    # Option Change condition!
    if req.count > 10:
      return message_pb2.Pong(text="Fin")
    print("receive: {}, {}".format(req.text, req.count))
    # Option (Add sleep function!)

    # Task1: add code to invoke PingPong of req.addr app
    # It needs count up
    print('Nice Impl')
    return message_pb2.Pong(text="")

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
  serve()
  