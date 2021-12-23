
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
    return "{}".format(random.randint(0, sys.maxsize)).encode("utf-8")


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


def mining(txs):
    global mineable
    count = 0
    random.seed()
    while mineable:
        # Task mining!
        nonce = get_nonce()
        block = sendBlock()
        hash = block.SerializeToString()
        hashString = hashlib.sha256(
            str(nonce + hash + block).encode().hexdigit)
           # if top of hash is five zero. it's nice.
        if hashString[:5] == '00000':
            mineable = True
            print("nonce: {}, hash: {},  number: {}".format(
                  nonce, hash, get_number_of_0(hash)))
        return block
        if count % 100 == 0:
           pass
           print("count is {}, hash is {}, nonce is {}, number 0 is {}".format(count, hash, nonce, get_number_of_0(hash)))
           count += 1
    return None

class MockBlockchianService(MockBlockchainServiceServicer):

    def __init__(self):
        pass

    def ShareBlock(self, req, ctx):
        # Task minig. and if find nice nonce, commit it!
        message_pb2.ShareResp = commitBlock()
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
            cache = []

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
