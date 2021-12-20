
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

from pbft.protos.message_pb2 import Tx

addr = ""
addrs = []
cache = []

block_chain = Blockchain()

def sendTx(addr, tx):
  with grpc.insecure_channel(addr) as channel:
    stub = message_pb2_grpc.SampleServiceStub(channel)
    response = stub.Share(tx)
    return response

def hash_sha3_256(msg):
  return hashlib.sha3_256(msg).hexdigest()

def get_number_of_0(hash):
  arr = re.findall('^0+', hash)
  if len(arr) == 0:
    return 0
  return len(arr[0])

def get_nonce():
  return "{}".format(random.randint(0, sys.maxsize)).encode("utf-8")

def sendBlock(addr, block):
  print("sendBlock", addr)
  with grpc.insecure_channel(addr) as channel:
    stub = message_pb2_grpc.MockBlockchainServiceStub(channel)
    response = stub.ShareBlock(block)
  return response  

def mining(txs):
  count = 0
  random.seed()
  while True:
    # Task mining!
    nonce = ...
    block = message_pb2.Block(txs=txs, nonce=nonce)
    hash = Hash(block)
    if hash is nice like a "0000024390ab2330903443" has five 0 on the top.:
      return block
    count += 1

class MockBlockchianService(MockBlockchainServiceServicer):

  def __init__(self):
    pass

  def ShareBlock(self, req, ctx):
    # Task minig. and if find nice nonce, commit it!
    # req is block
    block = mining(req.txs)
    commitBlock(block)
    return message_pb2.ShareResp(text="")

  def CommitBlock(self, req, ctx):    
    block_chain.save(req)

  def SendTx(self, req, ctx): 
    global cache
    print("received tx")
    cache.append(req)
    if len(cache) == 3:
      print("enough txs in cache, start broadcast")
      # Task: Make block and Broadcast it
      # make block
      block = message_pb2.Block(txs=txs, ....)
      for a in addrs:
        if a != addr:
          sendBlock(a, block)

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
  