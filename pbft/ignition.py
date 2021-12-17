
from pbft.protos import message_pb2_grpc
from pbft.protos import message_pb2
from pbft.protos.message_pb2_grpc import SampleServiceServicer
import grpc

addr = ""

def sendTx(addr, tx):
  with grpc.insecure_channel(addr) as channel:
    stub = message_pb2_grpc.SampleServiceStub(channel)
    response = stub.Share(tx)
    return response

tx = message_pb2.Tx(
  text="transfer",
  count=0,
  state = "req"
)
sendTx("localhost:50051", tx)