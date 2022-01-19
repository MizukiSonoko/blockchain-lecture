# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='message.proto',
  package='mock',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rmessage.proto\x12\x04mock\"?\n\x02Tx\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\r\n\x05\x63ount\x18\x02 \x01(\x05\x12\r\n\x05state\x18\x03 \x01(\t\x12\r\n\x05\x61\x64\x64rs\x18\x04 \x03(\t\"k\n\x05\x42lock\x12\x15\n\x03txs\x18\x01 \x03(\x0b\x32\x08.mock.Tx\x12\r\n\x05nonce\x18\x02 \x01(\t\x12\x0c\n\x04hash\x18\x03 \x01(\t\x12\x0c\n\x04prev\x18\x04 \x01(\t\x12\x11\n\ttimestamp\x18\x05 \x01(\x03\x12\r\n\x05state\x18\x06 \x01(\t\"\x19\n\tShareResp\x12\x0c\n\x04text\x18\x01 \x01(\t2\x9d\x01\n\x15MockBlockchainService\x12.\n\nShareBlock\x12\x0b.mock.Block\x1a\x0f.mock.ShareResp\"\x00\x30\x01\x12-\n\x0b\x43ommitBlock\x12\x0b.mock.Block\x1a\x0f.mock.ShareResp\"\x00\x12%\n\x06SendTx\x12\x08.mock.Tx\x1a\x0f.mock.ShareResp\"\x00\x62\x06proto3'
)




_TX = _descriptor.Descriptor(
  name='Tx',
  full_name='mock.Tx',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='mock.Tx.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='count', full_name='mock.Tx.count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='mock.Tx.state', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='addrs', full_name='mock.Tx.addrs', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=86,
)


_BLOCK = _descriptor.Descriptor(
  name='Block',
  full_name='mock.Block',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='txs', full_name='mock.Block.txs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nonce', full_name='mock.Block.nonce', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hash', full_name='mock.Block.hash', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='prev', full_name='mock.Block.prev', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='mock.Block.timestamp', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='mock.Block.state', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=88,
  serialized_end=195,
)


_SHARERESP = _descriptor.Descriptor(
  name='ShareResp',
  full_name='mock.ShareResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='mock.ShareResp.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=197,
  serialized_end=222,
)

_BLOCK.fields_by_name['txs'].message_type = _TX
DESCRIPTOR.message_types_by_name['Tx'] = _TX
DESCRIPTOR.message_types_by_name['Block'] = _BLOCK
DESCRIPTOR.message_types_by_name['ShareResp'] = _SHARERESP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Tx = _reflection.GeneratedProtocolMessageType('Tx', (_message.Message,), {
  'DESCRIPTOR' : _TX,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:mock.Tx)
  })
_sym_db.RegisterMessage(Tx)

Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), {
  'DESCRIPTOR' : _BLOCK,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:mock.Block)
  })
_sym_db.RegisterMessage(Block)

ShareResp = _reflection.GeneratedProtocolMessageType('ShareResp', (_message.Message,), {
  'DESCRIPTOR' : _SHARERESP,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:mock.ShareResp)
  })
_sym_db.RegisterMessage(ShareResp)



_MOCKBLOCKCHAINSERVICE = _descriptor.ServiceDescriptor(
  name='MockBlockchainService',
  full_name='mock.MockBlockchainService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=225,
  serialized_end=382,
  methods=[
  _descriptor.MethodDescriptor(
    name='ShareBlock',
    full_name='mock.MockBlockchainService.ShareBlock',
    index=0,
    containing_service=None,
    input_type=_BLOCK,
    output_type=_SHARERESP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CommitBlock',
    full_name='mock.MockBlockchainService.CommitBlock',
    index=1,
    containing_service=None,
    input_type=_BLOCK,
    output_type=_SHARERESP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SendTx',
    full_name='mock.MockBlockchainService.SendTx',
    index=2,
    containing_service=None,
    input_type=_TX,
    output_type=_SHARERESP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MOCKBLOCKCHAINSERVICE)

DESCRIPTOR.services_by_name['MockBlockchainService'] = _MOCKBLOCKCHAINSERVICE

# @@protoc_insertion_point(module_scope)
