

# https://docs.python.org/3/library/hashlib.html
import hashlib

def hash_sha3_256(msg):
  result = hashlib.sha3_512()
  result.update(msg) 
  return result.hexdigest()

def hash_sha3_256_file(path): 
  # Task2. Implement function using hashlib, open func
  return ''

if __name__ == '__main__':
  print(hash_sha3_256(b'hello from Bhutan')) # return '277e3e07d56684ec98cc2796b6f2127d36742d1de2c19deeba7ec4ebe04f788e'
  print(hash_sha3_256(b'')) # return 'a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a'
  print(hash_sha3_256_file('hash/data')) # return 'cd744fb79f53e2114ee04c0458a757d78cba94384c81bc64a1e5fad11c252897'
