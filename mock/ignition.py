
from mock.protos import message_pb2_grpc
from mock.protos import message_pb2
from mock.protos.message_pb2_grpc import MockBlockchainServiceStub
from google.protobuf import empty_pb2 
import sys
import grpc

addr = ""

def sendTxTo(addr, tx):
  with grpc.insecure_channel(addr) as channel:
    stub = message_pb2_grpc.MockBlockchainServiceStub(channel)
    resp = stub.SendTx(tx)
    return resp

def sendTx():
  tx = message_pb2.Tx(
    text="run some smart contract.",
    count=0,
    state = "req"
  )
  try:
    sendTxTo("localhost:50051", tx)
  except:
    pass 


def getChainFrom(addr):
  with grpc.insecure_channel(addr) as channel:
    stub = message_pb2_grpc.MockBlockchainServiceStub(channel)
    resp = stub.GetBlockChain(empty_pb2.Empty())
    return resp

def getChain():
  try:
    print("run chain")
    chain = getChainFrom("localhost:50051")
    for b in chain.blocks:
      print("+--------------------- --------------+---------------------------------------+")
      for tx in b.txs:
        print("| - Tx {:61}         |".format(tx.text))
      print("| ----------------                                                           |")
      print("| - Prev    {} |".format(b.prev))
      print("| - Creator {}                                                  | ".format(b.creator))
      print("| - Nonce   {:32}                                 |".format(b.nonce))
      print("+--------------------- --------------+---------------------------------------+")
      print("                                     | ")
      print("                                     | ")
  except Exception as e:
    print("e", e)
    pass 


def sendTx(ope):
  tx = message_pb2.Tx(
    text="run {}".format(ope),
    count=0,
    state = "req"
  )
  try:
    sendTxTo("localhost:50051", tx)
  except:
    pass 


if __name__ == '__main__':
  cmd = sys.argv[1]
  if cmd == "chain": 
    getChain()
  else:
    ope = sys.argv[2]
    sendTx(ope)