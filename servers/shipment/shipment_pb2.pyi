from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ShipmentConfirmation(_message.Message):
    __slots__ = ["aproximateDate"]
    APROXIMATEDATE_FIELD_NUMBER: _ClassVar[int]
    aproximateDate: str
    def __init__(self, aproximateDate: _Optional[str] = ...) -> None: ...

class TransactionResponse(_message.Message):
    __slots__ = ["status_code"]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    status_code: int
    def __init__(self, status_code: _Optional[int] = ...) -> None: ...

class getPackage(_message.Message):
    __slots__ = ["address", "id", "productQuantity"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCTQUANTITY_FIELD_NUMBER: _ClassVar[int]
    address: str
    id: str
    productQuantity: int
    def __init__(self, id: _Optional[str] = ..., address: _Optional[str] = ..., productQuantity: _Optional[int] = ...) -> None: ...
