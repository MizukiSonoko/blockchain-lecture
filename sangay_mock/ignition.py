
from mock.protos import message_pb2_grpc
from mock.protos import message_pb2
from mock.protos.message_pb2_grpc import MockBlockchainServiceStub
import grpc

addr = ""

def sendTx(addr, tx):
  with grpc.insecure_channel(addr) as channel:
    stub = message_pb2_grpc.MockBlockchainServiceStub(channel)
    response = stub.SendTx(tx)
    return response

tx = message_pb2.Tx(
  text="transfer",
  count=0,
  state = "req"
)
sendTx("localhost:50051", tx)