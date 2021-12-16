

# https://docs.python.org/3/library/hashlib.html
import hashlib

def hash_sha3_256(msg):
  # Task1. Implement function using hashlib
  # msg=(('hello from Bhutan').encode('utf-8'))
  str ='hello from Bhutan'    # initialize the message as a string
  result=hashlib.sha3_256()   #invoke the sha
  result.update(msg)
  return (result.hexdigest())

def hash_sha3_256_file(path): 
  # Task2. Implement function using hashlib, open func
  Data_Size=65330                               #Size of data in each read 64KB
  result=hashlib.sha3_256()
  with open("C:\\upgrade.log", 'rb') as myFile: #Open the file to read
    readFile=myFile.read(Data_Size)            #Read from the file in blocks
    while len(readFile)>0:                     #check if there is still data in the file
      result.update(readFile)                  #update the hash
      readFile=myFile.read(Data_Size)          #continue reading the file until len is 0
        
  return (result.hexdigest())

if __name__ == '__main__':
  print(hash_sha3_256(b'hello from Bhutan')) # return '277e3e07d56684ec98cc2796b6f2127d36742d1de2c19deeba7ec4ebe04f788e'
  print(hash_sha3_256(b'')) # return 'a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a'
  print(hash_sha3_256_file('hash/data')) # return 'cd744fb79f53e2114ee04c0458a757d78cba94384c81bc64a1e5fad11c252897'
