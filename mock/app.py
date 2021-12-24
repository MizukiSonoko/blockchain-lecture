from .mock.protos import message_pb2_grpc
from .mock.protos import message_pb2
from .mock.protos.message_pb2_grpc import MockBlockchainServiceServicer

#from mock.protos import message_pb2
f#rom mock.protos.message_pb2_grpc import MockBlockchainServiceServicer
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
mineable = True
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
    nonce= "{}".format(random.randint(0, sys.maxsize)).encode("utf-8")
    return nonce


def commitBlock(addr, block):
    with grpc.insecure_channel(addr) as channel:
        stub = message_pb2_grpc.MockBlockchainServiceStub(channel)
        resps = stub.CommitBlock(block)
        for r in resps:
            return r


def sendBlock(addr, block):
    print("sendBlock", addr)
    with grpc.insecure_channel(addr) as channel:
        stub = message_pb2_grpc.MockBlockchainServiceStub(channel)
        response = stub.ShareBlock(block)
    return response


def mining(block,txs,previous_hash,zero_prefix):
    while mineable:
      nonce = get_nonce()
      block_number=sendBlock()
      block_hash=(str(nonce) + str(block_number),previous_hash)
      new_block_hash=hashlib.sha3_256(block_hash).hexdigest()
    
      if get_number_of_0(new_block_hash)==5:
        print("nonce: {}, new_block_hash: {},  block_number: {}".format(
                  nonce, new_block_hash, get_number_of_0(hash)))
        return new_block_hash    
        
    
class MockBlockchianService(MockBlockchainServiceServicer):

    def __init__(self):
        pass

    def ShareBlock(self, req, ctx):
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
          executor = concurrent.futures.ThreadPoolExecutor(max_workers=4)
          resp.append(executor.submit(funcName(a, block)))
          for r in resp:
            r.result()
          #  -------
        else:
            print("stop mining because other node find nonce")
        
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
            block = message_pb2.Block(txs = cache, nonce = "")
            resp = []
            cache = []
            executor = concurrent.futures.ThreadPoolExecutor(max_workers=4)
            resp.append(executor.submit(funcName(a, block)))
            for r in resp:
              r.result()

        return message_pb2.ShareResp(text="")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    message_pb2_grpc.add_MockBlockchainServiceServicer_to_server(
        MockBlockchianService(), server)
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
