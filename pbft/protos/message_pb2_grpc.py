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
        self.Share = channel.unary_unary(
                '/pbft.SampleService/Share',
                request_serializer=message__pb2.Tx.SerializeToString,
                response_deserializer=message__pb2.ShareResp.FromString,
                )


class SampleServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Share(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SampleServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Share': grpc.unary_unary_rpc_method_handler(
                    servicer.Share,
                    request_deserializer=message__pb2.Tx.FromString,
                    response_serializer=message__pb2.ShareResp.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pbft.SampleService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SampleService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Share(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pbft.SampleService/Share',
            message__pb2.Tx.SerializeToString,
            message__pb2.ShareResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
