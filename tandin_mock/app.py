
from mock.protos import message_pb2_grpc
from mock.protos import message_pb2
from mock.protos.message_pb2_grpc import MockBlockchainServiceServicer
from chain import Blockchain
import grpc
from concurrent import futures
import time
import concurrent.futures
from concurrent.futures import ProcessPoolExecutor
import time
import sys
import re 
import hashlib
import random
import asyncio

addr = ""
addrs = []
cache = []
miningable = True

block_chain = Blockchain()

# Send Tx to other nodes
def sendTx(addr, tx):
  with grpc.insecure_channel(addr) as channel:
    stub = message_pb2_grpc.SampleServiceStub(channel)
    responses = stub.Share(tx)
    return responses

# Caluclate hash from arguments msg. msg is b'text'
def hash_sha3_256(msg):
  return hashlib.sha3_256(msg).hexdigest()

# Return number of '0' on the top of argumented hash.
# When hash is '00000a964f8465d7deb738ae1c7c723f5ad690276c94a5ab88cd1c0d5a3205142', returns 5
# When hash is 'a0000a964f8465d7deb738ae1c7c723f5ad690276c94a5ab88cd1c0d5a3205142', returns 0
def get_number_of_0(hash):
  arr = re.findall('^0+', hash)
  if len(arr) == 0:
    return 0
  return len(arr[0])

# Get random string called nonce like '1329742803242'
def get_nonce():
  return "{}".format(random.randint(0, sys.maxsize)).encode("utf-8")

# Send block as commited block
def commitBlock(addr, block):
  with grpc.insecure_channel(addr) as channel:
    stub = message_pb2_grpc.MockBlockchainServiceStub(channel)
    resps = stub.CommitBlock(block)
    for r in resps:
      return r  


# Send block as un-commited block, it means not confirmed.
def sendBlock(addr, block):
  print("sendBlock", addr)
  with grpc.insecure_channel(addr) as channel:
    stub = message_pb2_grpc.MockBlockchainServiceStub(channel)
    resps = stub.ShareBlock(block)
    for r in resps:
      return r  

def mining(txs):
  global miningable
  count = 0
  random.seed()
  last = block_chain.top()
  last_block_hash= hash_sha3_256(last.SerializeToString())
  while miningable:       
    # Add your implements
    nonce = get_nonce() # initialize nonce as random string 
    # initialize block contain txs and nonce
    block = message_pb2.Block(
      txs =txs,
      nonce = nonce,
      prev = last_block_hash,
      creator = addr
    )
    hash = ... # calucate hash from `block.SerializeToString()`. block.SerializeToString() is serialized string
    if ...: # if top of hash is five zero. it's nice.
      print("nonce: {}, hash: {},  number: {}".format(nonce, hash, get_number_of_0(hash)))
      return block

    # This is only logs.
    if count % 100 == 0:
      pass
      #print("count is {}, hash is {}, nonce is {}, number 0 is {}".format(count, hash, nonce, get_number_of_0(hash)))
    count += 1
  return None

class MockBlockchianService(MockBlockchainServiceServicer):

  def __init__(self):
    pass

  def ShareBlock(self, req, ctx):
    # Pleaze ignore.
    global miningable
    yield message_pb2.ShareResp(text="")

    miningable = True
    block = mining(req.txs)
    if block:
      print("find!")
      resp = []
      # Add implement, send commited block to other nodes.
      # note. it requires Asynchronous. you should use ThreadPoolExecutor like this
      # -------
      # executor = concurrent.futures.ThreadPoolExecutor(max_workers=4)
      # resp.append(executor.submit(funcName(a, block)))
      # for r in resp:
      #   r.result()
      # -------
      ...
    else:
      print("stop mining because other node find nonce")
    
    return message_pb2.ShareResp(text="")

  def CommitBlock(self, req, ctx):
    global miningable
    yield message_pb2.ShareResp(text="")
    miningable = False
    # Add implement, save block to blockchain
    ...

  def SendTx(self, req, ctx): 
    global cache
    print("received tx")
    cache.append(req)
    if len(cache) == 3:
      print("enough txs in cache, start broadcast")
      block = message_pb2.Block(txs = cache, nonce = "")
      resp = []
      # Add implement, send un-commited block to other nodes.
      # note. it requires Asynchronous. you should use ThreadPoolExecutor like this
      # -------
      # executor = concurrent.futures.ThreadPoolExecutor(max_workers=4)
      # resp.append(executor.submit(funcName(a, block)))
      # for r in resp:
      #   r.result()
      # -------
      cache = []
    
    return message_pb2.ShareResp(text="")

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  message_pb2_grpc.add_MockBlockchainServiceServicer_to_server(MockBlockchianService(), server)
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
  