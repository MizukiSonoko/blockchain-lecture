

from mock.protos import message_pb2
import hashlib

class Blockchain:

  def __init__(self) -> None:
    self.blockchain = []

  def save(self, block):
    if len(self.blockchain) == 0:
      self.blockchain = [block]
    else: 
      last_block = self.blockchain[-1]
      new_block = message_pb2.Block(
        txs = block.txs,
        nonce = block.nonce,
        prev = last_block.hash,
      )
      hash = hashlib.sha3_256(new_block.SerializeToString()).hexdigest()
      new_block.hash = hash
      self.blockchain.append(block)

  def chain(self):
    return self.blockchain

  def top(self):
    if len(self.blockchain) == 0:
      return message_pb2.Block()
    return self.blockchain[-1]