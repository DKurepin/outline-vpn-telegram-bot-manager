# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: country.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'country.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rcountry.proto\x12\x05proto\x1a\x1bgoogle/protobuf/empty.proto\"#\n\x07\x43ountry\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\".\n\tCountries\x12!\n\tcountries\x18\x01 \x03(\x0b\x32\x0e.proto.Country\"\x1b\n\x0b\x43ountryName\x12\x0c\n\x04name\x18\x01 \x01(\t\"0\n\x14\x43ountryCreateRequest\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t2\xc3\x01\n\x0e\x43ountryService\x12;\n\x0fGetAllCountries\x12\x16.google.protobuf.Empty\x1a\x10.proto.Countries\x12\x36\n\x10GetCountryByName\x12\x12.proto.CountryName\x1a\x0e.proto.Country\x12<\n\rCreateCountry\x12\x1b.proto.CountryCreateRequest\x1a\x0e.proto.Countryb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'country_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_COUNTRY']._serialized_start=53
  _globals['_COUNTRY']._serialized_end=88
  _globals['_COUNTRIES']._serialized_start=90
  _globals['_COUNTRIES']._serialized_end=136
  _globals['_COUNTRYNAME']._serialized_start=138
  _globals['_COUNTRYNAME']._serialized_end=165
  _globals['_COUNTRYCREATEREQUEST']._serialized_start=167
  _globals['_COUNTRYCREATEREQUEST']._serialized_end=215
  _globals['_COUNTRYSERVICE']._serialized_start=218
  _globals['_COUNTRYSERVICE']._serialized_end=413
# @@protoc_insertion_point(module_scope)
