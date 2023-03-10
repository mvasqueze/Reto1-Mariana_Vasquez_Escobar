# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import shoppingCart_pb2 as shoppingCart__pb2


class ShoppingCartStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddProduct = channel.unary_unary(
                '/ShoppingCart/AddProduct',
                request_serializer=shoppingCart__pb2.addToOrder.SerializeToString,
                response_deserializer=shoppingCart__pb2.TransactionResponse.FromString,
                )
        self.ConfirmOrder = channel.unary_unary(
                '/ShoppingCart/ConfirmOrder',
                request_serializer=shoppingCart__pb2.confirmOrder.SerializeToString,
                response_deserializer=shoppingCart__pb2.TransactionResponse.FromString,
                )


class ShoppingCartServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfirmOrder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ShoppingCartServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.AddProduct,
                    request_deserializer=shoppingCart__pb2.addToOrder.FromString,
                    response_serializer=shoppingCart__pb2.TransactionResponse.SerializeToString,
            ),
            'ConfirmOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfirmOrder,
                    request_deserializer=shoppingCart__pb2.confirmOrder.FromString,
                    response_serializer=shoppingCart__pb2.TransactionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ShoppingCart', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ShoppingCart(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ShoppingCart/AddProduct',
            shoppingCart__pb2.addToOrder.SerializeToString,
            shoppingCart__pb2.TransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfirmOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ShoppingCart/ConfirmOrder',
            shoppingCart__pb2.confirmOrder.SerializeToString,
            shoppingCart__pb2.TransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
