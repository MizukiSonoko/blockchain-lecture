# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import message_pb2 as message__pb2


class SampleServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Hello = channel.unary_unary(
                '/p2p.SampleService/Hello',
                request_serializer=message__pb2.SimpleReq.SerializeToString,
                response_deserializer=message__pb2.SimpleResp.FromString,
                )
        self.PingPong = channel.unary_unary(
                '/p2p.SampleService/PingPong',
                request_serializer=message__pb2.Ping.SerializeToString,
                response_deserializer=message__pb2.Pong.FromString,
                )


class SampleServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Hello(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PingPong(self, request, context):
        """Task: Implement it!
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SampleServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Hello': grpc.unary_unary_rpc_method_handler(
                    servicer.Hello,
                    request_deserializer=message__pb2.SimpleReq.FromString,
                    response_serializer=message__pb2.SimpleResp.SerializeToString,
            ),
            'PingPong': grpc.unary_unary_rpc_method_handler(
                    servicer.PingPong,
                    request_deserializer=message__pb2.Ping.FromString,
                    response_serializer=message__pb2.Pong.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'p2p.SampleService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SampleService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Hello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/p2p.SampleService/Hello',
            message__pb2.SimpleReq.SerializeToString,
            message__pb2.SimpleResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PingPong(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/p2p.SampleService/PingPong',
            message__pb2.Ping.SerializeToString,
            message__pb2.Pong.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
