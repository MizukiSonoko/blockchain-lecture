import hashlib

# https://pycryptodome.readthedocs.io/en/latest/src/introduction.html
from Crypto.Hash import SHA256
from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
import base64

def generate_pri_pem():
  key = ECC.generate(curve='P-256')
  return key.export_key(format='PEM')

def restore_key_from_pem(pem):
  return ECC.import_key(pem)

def generate_pub_pem(key):
  return key.public_key().export_key(format='PEM')

key_pri_pem = generate_pri_pem()
key = restore_key_from_pem(key_pri_pem)
pub_key_pem = generate_pub_pem(key)

def sign(prikey, message):
  # Task: Hash message
  hashed_message = None
  # Task: Sign hashed_message using signer
  signer = DSS.new(prikey, 'fips-186-3')
  # Sign
  signature = None
  return signature

message = b'Hello!'
signature = sign(key, message)

pubKey = restore_key_from_pem(pub_key_pem)

def verify(message, pub_key):
  # Task Hash message
  hashed_message = None
  try:
      verifier = DSS.new(pubKey, 'fips-186-3')
      # Task: Verify hashed_message using verifier
      print("Passed")
  except ValueError:
      print("Failed")
