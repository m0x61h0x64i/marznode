# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app/dns/config.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from marznode.xray_api.proto.common.net import address_pb2 as common_dot_net_dot_address__pb2
from marznode.xray_api.proto.common.net import destination_pb2 as common_dot_net_dot_destination__pb2
from marznode.xray_api.proto.app.router import config_pb2 as app_dot_router_dot_config__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x61pp/dns/config.proto\x12\x0cxray.app.dns\x1a\x18\x63ommon/net/address.proto\x1a\x1c\x63ommon/net/destination.proto\x1a\x17\x61pp/router/config.proto\"\xbf\x03\n\nNameServer\x12*\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32\x19.xray.common.net.Endpoint\x12\x11\n\tclient_ip\x18\x05 \x01(\x0c\x12\x14\n\x0cskipFallback\x18\x06 \x01(\x08\x12\x43\n\x12prioritized_domain\x18\x02 \x03(\x0b\x32\'.xray.app.dns.NameServer.PriorityDomain\x12%\n\x05geoip\x18\x03 \x03(\x0b\x32\x16.xray.app.router.GeoIP\x12=\n\x0eoriginal_rules\x18\x04 \x03(\x0b\x32%.xray.app.dns.NameServer.OriginalRule\x12\x33\n\x0equery_strategy\x18\x07 \x01(\x0e\x32\x1b.xray.app.dns.QueryStrategy\x1aP\n\x0ePriorityDomain\x12.\n\x04type\x18\x01 \x01(\x0e\x32 .xray.app.dns.DomainMatchingType\x12\x0e\n\x06\x64omain\x18\x02 \x01(\t\x1a*\n\x0cOriginalRule\x12\x0c\n\x04rule\x18\x01 \x01(\t\x12\x0c\n\x04size\x18\x02 \x01(\r\"\xbf\x04\n\x06\x43onfig\x12\x32\n\x0bNameServers\x18\x01 \x03(\x0b\x32\x19.xray.common.net.EndpointB\x02\x18\x01\x12-\n\x0bname_server\x18\x05 \x03(\x0b\x32\x18.xray.app.dns.NameServer\x12\x32\n\x05Hosts\x18\x02 \x03(\x0b\x32\x1f.xray.app.dns.Config.HostsEntryB\x02\x18\x01\x12\x11\n\tclient_ip\x18\x03 \x01(\x0c\x12\x36\n\x0cstatic_hosts\x18\x04 \x03(\x0b\x32 .xray.app.dns.Config.HostMapping\x12\x0b\n\x03tag\x18\x06 \x01(\t\x12\x14\n\x0c\x64isableCache\x18\x08 \x01(\x08\x12\x33\n\x0equery_strategy\x18\t \x01(\x0e\x32\x1b.xray.app.dns.QueryStrategy\x12\x17\n\x0f\x64isableFallback\x18\n \x01(\x08\x12\x1e\n\x16\x64isableFallbackIfMatch\x18\x0b \x01(\x08\x1aI\n\nHostsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12*\n\x05value\x18\x02 \x01(\x0b\x32\x1b.xray.common.net.IPOrDomain:\x02\x38\x01\x1aq\n\x0bHostMapping\x12.\n\x04type\x18\x01 \x01(\x0e\x32 .xray.app.dns.DomainMatchingType\x12\x0e\n\x06\x64omain\x18\x02 \x01(\t\x12\n\n\x02ip\x18\x03 \x03(\x0c\x12\x16\n\x0eproxied_domain\x18\x04 \x01(\tJ\x04\x08\x07\x10\x08*E\n\x12\x44omainMatchingType\x12\x08\n\x04\x46ull\x10\x00\x12\r\n\tSubdomain\x10\x01\x12\x0b\n\x07Keyword\x10\x02\x12\t\n\x05Regex\x10\x03*5\n\rQueryStrategy\x12\n\n\x06USE_IP\x10\x00\x12\x0b\n\x07USE_IP4\x10\x01\x12\x0b\n\x07USE_IP6\x10\x02\x42\x46\n\x10\x63om.xray.app.dnsP\x01Z!github.com/xtls/xray-core/app/dns\xaa\x02\x0cXray.App.Dnsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app.dns.config_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\020com.xray.app.dnsP\001Z!github.com/xtls/xray-core/app/dns\252\002\014Xray.App.Dns'
  _globals['_CONFIG_HOSTSENTRY']._options = None
  _globals['_CONFIG_HOSTSENTRY']._serialized_options = b'8\001'
  _globals['_CONFIG'].fields_by_name['NameServers']._options = None
  _globals['_CONFIG'].fields_by_name['NameServers']._serialized_options = b'\030\001'
  _globals['_CONFIG'].fields_by_name['Hosts']._options = None
  _globals['_CONFIG'].fields_by_name['Hosts']._serialized_options = b'\030\001'
  _globals['_DOMAINMATCHINGTYPE']._serialized_start=1147
  _globals['_DOMAINMATCHINGTYPE']._serialized_end=1216
  _globals['_QUERYSTRATEGY']._serialized_start=1218
  _globals['_QUERYSTRATEGY']._serialized_end=1271
  _globals['_NAMESERVER']._serialized_start=120
  _globals['_NAMESERVER']._serialized_end=567
  _globals['_NAMESERVER_PRIORITYDOMAIN']._serialized_start=443
  _globals['_NAMESERVER_PRIORITYDOMAIN']._serialized_end=523
  _globals['_NAMESERVER_ORIGINALRULE']._serialized_start=525
  _globals['_NAMESERVER_ORIGINALRULE']._serialized_end=567
  _globals['_CONFIG']._serialized_start=570
  _globals['_CONFIG']._serialized_end=1145
  _globals['_CONFIG_HOSTSENTRY']._serialized_start=951
  _globals['_CONFIG_HOSTSENTRY']._serialized_end=1024
  _globals['_CONFIG_HOSTMAPPING']._serialized_start=1026
  _globals['_CONFIG_HOSTMAPPING']._serialized_end=1139
# @@protoc_insertion_point(module_scope)
