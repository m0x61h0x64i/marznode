# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: app/proxyman/command/command.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import marznode.xray_api.proto.common.protocol.user_pb2
import marznode.xray_api.proto.common.serial.typed_message_pb2
import marznode.xray_api.proto.core.config_pb2
import marznode.xray_api.proto.app.proxyman.command.command_pb2


class HandlerServiceBase(abc.ABC):

    @abc.abstractmethod
    async def AddInbound(self, stream: 'grpclib.server.Stream[app.proxyman.command.command_pb2.AddInboundRequest, app.proxyman.command.command_pb2.AddInboundResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RemoveInbound(self, stream: 'grpclib.server.Stream[app.proxyman.command.command_pb2.RemoveInboundRequest, app.proxyman.command.command_pb2.RemoveInboundResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AlterInbound(self, stream: 'grpclib.server.Stream[app.proxyman.command.command_pb2.AlterInboundRequest, app.proxyman.command.command_pb2.AlterInboundResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AddOutbound(self, stream: 'grpclib.server.Stream[app.proxyman.command.command_pb2.AddOutboundRequest, app.proxyman.command.command_pb2.AddOutboundResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RemoveOutbound(self, stream: 'grpclib.server.Stream[app.proxyman.command.command_pb2.RemoveOutboundRequest, app.proxyman.command.command_pb2.RemoveOutboundResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AlterOutbound(self, stream: 'grpclib.server.Stream[app.proxyman.command.command_pb2.AlterOutboundRequest, app.proxyman.command.command_pb2.AlterOutboundResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/xray.app.proxyman.command.HandlerService/AddInbound': grpclib.const.Handler(
                self.AddInbound,
                grpclib.const.Cardinality.UNARY_UNARY,
                marznode.xray_api.proto.app.proxyman.command.command_pb2.AddInboundRequest,
                marznode.xray_api.proto.app.proxyman.command.command_pb2.AddInboundResponse,
            ),
            '/xray.app.proxyman.command.HandlerService/RemoveInbound': grpclib.const.Handler(
                self.RemoveInbound,
                grpclib.const.Cardinality.UNARY_UNARY,
                marznode.xray_api.proto.app.proxyman.command.command_pb2.RemoveInboundRequest,
                marznode.xray_api.proto.app.proxyman.command.command_pb2.RemoveInboundResponse,
            ),
            '/xray.app.proxyman.command.HandlerService/AlterInbound': grpclib.const.Handler(
                self.AlterInbound,
                grpclib.const.Cardinality.UNARY_UNARY,
                marznode.xray_api.proto.app.proxyman.command.command_pb2.AlterInboundRequest,
                marznode.xray_api.proto.app.proxyman.command.command_pb2.AlterInboundResponse,
            ),
            '/xray.app.proxyman.command.HandlerService/AddOutbound': grpclib.const.Handler(
                self.AddOutbound,
                grpclib.const.Cardinality.UNARY_UNARY,
                marznode.xray_api.proto.app.proxyman.command.command_pb2.AddOutboundRequest,
                marznode.xray_api.proto.app.proxyman.command.command_pb2.AddOutboundResponse,
            ),
            '/xray.app.proxyman.command.HandlerService/RemoveOutbound': grpclib.const.Handler(
                self.RemoveOutbound,
                grpclib.const.Cardinality.UNARY_UNARY,
                marznode.xray_api.proto.app.proxyman.command.command_pb2.RemoveOutboundRequest,
                marznode.xray_api.proto.app.proxyman.command.command_pb2.RemoveOutboundResponse,
            ),
            '/xray.app.proxyman.command.HandlerService/AlterOutbound': grpclib.const.Handler(
                self.AlterOutbound,
                grpclib.const.Cardinality.UNARY_UNARY,
                marznode.xray_api.proto.app.proxyman.command.command_pb2.AlterOutboundRequest,
                marznode.xray_api.proto.app.proxyman.command.command_pb2.AlterOutboundResponse,
            ),
        }


class HandlerServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.AddInbound = grpclib.client.UnaryUnaryMethod(
            channel,
            '/xray.app.proxyman.command.HandlerService/AddInbound',
            marznode.xray_api.proto.app.proxyman.command.command_pb2.AddInboundRequest,
            marznode.xray_api.proto.app.proxyman.command.command_pb2.AddInboundResponse,
        )
        self.RemoveInbound = grpclib.client.UnaryUnaryMethod(
            channel,
            '/xray.app.proxyman.command.HandlerService/RemoveInbound',
            marznode.xray_api.proto.app.proxyman.command.command_pb2.RemoveInboundRequest,
            marznode.xray_api.proto.app.proxyman.command.command_pb2.RemoveInboundResponse,
        )
        self.AlterInbound = grpclib.client.UnaryUnaryMethod(
            channel,
            '/xray.app.proxyman.command.HandlerService/AlterInbound',
            marznode.xray_api.proto.app.proxyman.command.command_pb2.AlterInboundRequest,
            marznode.xray_api.proto.app.proxyman.command.command_pb2.AlterInboundResponse,
        )
        self.AddOutbound = grpclib.client.UnaryUnaryMethod(
            channel,
            '/xray.app.proxyman.command.HandlerService/AddOutbound',
            marznode.xray_api.proto.app.proxyman.command.command_pb2.AddOutboundRequest,
            marznode.xray_api.proto.app.proxyman.command.command_pb2.AddOutboundResponse,
        )
        self.RemoveOutbound = grpclib.client.UnaryUnaryMethod(
            channel,
            '/xray.app.proxyman.command.HandlerService/RemoveOutbound',
            marznode.xray_api.proto.app.proxyman.command.command_pb2.RemoveOutboundRequest,
            marznode.xray_api.proto.app.proxyman.command.command_pb2.RemoveOutboundResponse,
        )
        self.AlterOutbound = grpclib.client.UnaryUnaryMethod(
            channel,
            '/xray.app.proxyman.command.HandlerService/AlterOutbound',
            marznode.xray_api.proto.app.proxyman.command.command_pb2.AlterOutboundRequest,
            marznode.xray_api.proto.app.proxyman.command.command_pb2.AlterOutboundResponse,
        )
