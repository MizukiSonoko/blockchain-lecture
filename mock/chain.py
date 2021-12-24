

from mock.protos import message_pb2
import hashlib

class Blockchain:

  def __init__(self) -> None:
    self.chain = []

  def save(self, block):
    if len(self.chain) == 0:
      self.chain = [block]
    else: 
      last_block = self.chain[-1]
      new_block = message_pb2.Block(
        txs = block.txs,
        nonce = block.nonce,
        prev = last_block.hash,
      )
      hash = hashlib.sha3_256(new_block.SerializeToString()).hexdigest()
      new_block.hash = hash
      self.push(new_block)
