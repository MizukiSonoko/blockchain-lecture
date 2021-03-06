# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import message_pb2 as message__pb2


class MockBlockchainServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.
        Args:
            channel: A grpc.Channel.
        """
        self.ShareBlock = channel.unary_stream(
                '/MockBlockchainService/ShareBlock',
                request_serializer=message__pb2.Block.SerializeToString,
                response_deserializer=message__pb2.ShareResp.FromString,
                )
        self.CommitBlock = channel.unary_stream(
                '/MockBlockchainService/CommitBlock',
                request_serializer=message__pb2.Block.SerializeToString,
                response_deserializer=message__pb2.ShareResp.FromString,
                )
        self.SendTx = channel.unary_unary(
                '/MockBlockchainService/SendTx',
                request_serializer=message__pb2.Tx.SerializeToString,
                response_deserializer=message__pb2.ShareResp.FromString,
                )
        self.GetBlockChain = channel.unary_unary(
                '/MockBlockchainService/GetBlockChain',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=message__pb2.BlockChain.FromString,
                )


class MockBlockchainServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ShareBlock(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CommitBlock(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendTx(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBlockChain(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MockBlockchainServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ShareBlock': grpc.unary_stream_rpc_method_handler(
                    servicer.ShareBlock,
                    request_deserializer=message__pb2.Block.FromString,
                    response_serializer=message__pb2.ShareResp.SerializeToString,
            ),
            'CommitBlock': grpc.unary_stream_rpc_method_handler(
                    servicer.CommitBlock,
                    request_deserializer=message__pb2.Block.FromString,
                    response_serializer=message__pb2.ShareResp.SerializeToString,
            ),
            'SendTx': grpc.unary_unary_rpc_method_handler(
                    servicer.SendTx,
                    request_deserializer=message__pb2.Tx.FromString,
                    response_serializer=message__pb2.ShareResp.SerializeToString,
            ),
            'GetBlockChain': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBlockChain,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=message__pb2.BlockChain.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            #removed mock from mock.Mock...
            'MockBlockchainService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MockBlockchainService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ShareBlock(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/MockBlockchainService/ShareBlock',
            message__pb2.Block.SerializeToString,
            message__pb2.ShareResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CommitBlock(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/MockBlockchainService/CommitBlock',
            message__pb2.Block.SerializeToString,
            message__pb2.ShareResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendTx(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):   #removed /mock. from /mock.MockBloc....
        return grpc.experimental.unary_unary(request, target, '/MockBlockchainService/SendTx',
            message__pb2.Tx.SerializeToString,
            message__pb2.ShareResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBlockChain(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MockBlockchainService/GetBlockChain',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            message__pb2.BlockChain.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

   