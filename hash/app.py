

# https://docs.python.org/3/library/hashlib.html
import hashlib

def hash_sha3_256(msg):
  # Task1. Implement function using hashlib
  x = hashlib.sha256()
  x.update(msg)
  return (x.hexdigest())

def hash_sha3_256_file(path): 
  # Task2. Implement function using hashlib, open func

    BLOCKSIZE = 65536
    hasher = hashlib.md5()
    with open("/Users/pixcy/Desktop/pema.pdf", 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    return hasher.hexdigest() 
if __name__ == '__main__':
  print("The Hash value of is :" + hash_sha3_256(b'hello from Bhutan')) # return '277e3e07d56684ec98cc2796b6f2127d36742d1de2c19deeba7ec4ebe04f788e'
  print(hash_sha3_256(b'hi')) # return 'a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a'
  print(hash_sha3_256_file('hash/data')) # return 'cd744fb79f53e2114ee04c0458a757d78cba94384c81bc64a1e5fad11c252897'
