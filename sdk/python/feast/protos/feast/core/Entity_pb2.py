# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feast/core/Entity.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2

from feast.protos.feast.types import Value_pb2 as feast_dot_types_dot_Value__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
  name='feast/core/Entity.proto',
  package='feast.core',
  syntax='proto3',
  serialized_options=b'\n\020feast.proto.coreB\013EntityProtoZ3github.com/feast-dev/feast/sdk/go/protos/feast/core',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x17\x66\x65\x61st/core/Entity.proto\x12\nfeast.core\x1a\x17\x66\x65\x61st/types/Value.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"V\n\x06\x45ntity\x12&\n\x04spec\x18\x01 \x01(\x0b\x32\x18.feast.core.EntitySpecV2\x12$\n\x04meta\x18\x02 \x01(\x0b\x32\x16.feast.core.EntityMeta\"\xd8\x01\n\x0c\x45ntitySpecV2\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07project\x18\t \x01(\t\x12/\n\nvalue_type\x18\x02 \x01(\x0e\x32\x1b.feast.types.ValueType.Enum\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x34\n\x06labels\x18\x08 \x03(\x0b\x32$.feast.core.EntitySpecV2.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x7f\n\nEntityMeta\x12\x35\n\x11\x63reated_timestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12:\n\x16last_updated_timestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampBT\n\x10\x66\x65\x61st.proto.coreB\x0b\x45ntityProtoZ3github.com/feast-dev/feast/sdk/go/protos/feast/coreb\x06proto3'
  ,
  dependencies=[feast_dot_types_dot_Value__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_ENTITY = _descriptor.Descriptor(
  name='Entity',
  full_name='feast.core.Entity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='spec', full_name='feast.core.Entity.spec', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='meta', full_name='feast.core.Entity.meta', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=97,
  serialized_end=183,
)


_ENTITYSPECV2_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='feast.core.EntitySpecV2.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='feast.core.EntitySpecV2.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='feast.core.EntitySpecV2.LabelsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=357,
  serialized_end=402,
)

_ENTITYSPECV2 = _descriptor.Descriptor(
  name='EntitySpecV2',
  full_name='feast.core.EntitySpecV2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='feast.core.EntitySpecV2.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='project', full_name='feast.core.EntitySpecV2.project', index=1,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value_type', full_name='feast.core.EntitySpecV2.value_type', index=2,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='feast.core.EntitySpecV2.description', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='feast.core.EntitySpecV2.labels', index=4,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_ENTITYSPECV2_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=186,
  serialized_end=402,
)


_ENTITYMETA = _descriptor.Descriptor(
  name='EntityMeta',
  full_name='feast.core.EntityMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='created_timestamp', full_name='feast.core.EntityMeta.created_timestamp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_updated_timestamp', full_name='feast.core.EntityMeta.last_updated_timestamp', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=404,
  serialized_end=531,
)

_ENTITY.fields_by_name['spec'].message_type = _ENTITYSPECV2
_ENTITY.fields_by_name['meta'].message_type = _ENTITYMETA
_ENTITYSPECV2_LABELSENTRY.containing_type = _ENTITYSPECV2
_ENTITYSPECV2.fields_by_name['value_type'].enum_type = feast_dot_types_dot_Value__pb2._VALUETYPE_ENUM
_ENTITYSPECV2.fields_by_name['labels'].message_type = _ENTITYSPECV2_LABELSENTRY
_ENTITYMETA.fields_by_name['created_timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ENTITYMETA.fields_by_name['last_updated_timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['Entity'] = _ENTITY
DESCRIPTOR.message_types_by_name['EntitySpecV2'] = _ENTITYSPECV2
DESCRIPTOR.message_types_by_name['EntityMeta'] = _ENTITYMETA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Entity = _reflection.GeneratedProtocolMessageType('Entity', (_message.Message,), {
  'DESCRIPTOR' : _ENTITY,
  '__module__' : 'feast.core.Entity_pb2'
  # @@protoc_insertion_point(class_scope:feast.core.Entity)
  })
_sym_db.RegisterMessage(Entity)

EntitySpecV2 = _reflection.GeneratedProtocolMessageType('EntitySpecV2', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _ENTITYSPECV2_LABELSENTRY,
    '__module__' : 'feast.core.Entity_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.EntitySpecV2.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _ENTITYSPECV2,
  '__module__' : 'feast.core.Entity_pb2'
  # @@protoc_insertion_point(class_scope:feast.core.EntitySpecV2)
  })
_sym_db.RegisterMessage(EntitySpecV2)
_sym_db.RegisterMessage(EntitySpecV2.LabelsEntry)

EntityMeta = _reflection.GeneratedProtocolMessageType('EntityMeta', (_message.Message,), {
  'DESCRIPTOR' : _ENTITYMETA,
  '__module__' : 'feast.core.Entity_pb2'
  # @@protoc_insertion_point(class_scope:feast.core.EntityMeta)
  })
_sym_db.RegisterMessage(EntityMeta)


DESCRIPTOR._options = None
_ENTITYSPECV2_LABELSENTRY._options = None
# @@protoc_insertion_point(module_scope)