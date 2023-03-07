from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Package(_message.Message):
    __slots__ = ["address", "productQuantity"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PRODUCTQUANTITY_FIELD_NUMBER: _ClassVar[int]
    address: str
    productQuantity: int
    def __init__(self, address: _Optional[str] = ..., productQuantity: _Optional[int] = ...) -> None: ...

class ShipmentConfirmation(_message.Message):
    __slots__ = ["aproximateDate"]
    APROXIMATEDATE_FIELD_NUMBER: _ClassVar[int]
    aproximateDate: str
    def __init__(self, aproximateDate: _Optional[str] = ...) -> None: ...
