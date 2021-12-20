#
# https://docs.python.org/3/library/hashlib.html
import hashlib
from os import read

def hash_sha3_256(msg):
  hash_obj = hashlib.sha3_256( ) # Call the hash funcstion in this case sha3_256
  hash_obj.update(msg) # Update the hash function with msg parameter passed.
  return hash_obj.hexdigest()

def hash_sha3_256_file(path): 
  # Task2. Implement function using hashlib, open func
  h = hashlib.sha3_256()
  with open(path,'rb') as file: # read file in binary mode r-read, b-binary
    fread = 0
    while fread != b'':   # read till the end of the binary file.
          fread=file.read()
          h.update(fread)
  return h.hexdigest()

if __name__ == '__main__':
  print(hash_sha3_256(b'hello from Bhutan')) # return '277e3e07d56684ec98cc2796b6f2127d36742d1de2c19deeba7ec4ebe04f788e'
  print(hash_sha3_256(b'')) # return 'a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a'
  print(hash_sha3_256_file('hash/data')) # return 'cd744fb79f53e2114ee04c0458a757d78cba94384c81bc64a1e5fad11c252897'
