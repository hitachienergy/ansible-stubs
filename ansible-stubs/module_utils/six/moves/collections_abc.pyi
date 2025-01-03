import abc
from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod
from collections.abc import Generator as _Generator

__all__ = ['Awaitable', 'Coroutine', 'AsyncIterable', 'AsyncIterator', 'AsyncGenerator', 'Hashable', 'Iterable', 'Iterator', 'Generator', 'Reversible', 'Sized', 'Container', 'Callable', 'Collection', 'Set', 'MutableSet', 'Mapping', 'MutableMapping', 'MappingView', 'KeysView', 'ItemsView', 'ValuesView', 'Sequence', 'MutableSequence', 'ByteString', 'Buffer']

class Hashable(metaclass=ABCMeta):
    @abstractmethod
    def __hash__(self): ...
    @classmethod
    def __subclasshook__(cls, C): ...

class Awaitable(metaclass=ABCMeta):
    @abstractmethod
    def __await__(self): ...
    @classmethod
    def __subclasshook__(cls, C): ...
    __class_getitem__: Incomplete

class Coroutine(Awaitable, metaclass=abc.ABCMeta):
    @abstractmethod
    def send(self, value): ...
    @abstractmethod
    def throw(self, typ, val: Incomplete | None = None, tb: Incomplete | None = None): ...
    def close(self) -> None: ...
    @classmethod
    def __subclasshook__(cls, C): ...

class AsyncIterable(metaclass=ABCMeta):
    @abstractmethod
    def __aiter__(self): ...
    @classmethod
    def __subclasshook__(cls, C): ...
    __class_getitem__: Incomplete

class AsyncIterator(AsyncIterable, metaclass=abc.ABCMeta):
    @abstractmethod
    async def __anext__(self): ...
    def __aiter__(self): ...
    @classmethod
    def __subclasshook__(cls, C): ...

class AsyncGenerator(AsyncIterator, metaclass=abc.ABCMeta):
    async def __anext__(self): ...
    @abstractmethod
    async def asend(self, value): ...
    @abstractmethod
    async def athrow(self, typ, val: Incomplete | None = None, tb: Incomplete | None = None): ...
    async def aclose(self) -> None: ...
    @classmethod
    def __subclasshook__(cls, C): ...

class Iterable(metaclass=ABCMeta):
    @abstractmethod
    def __iter__(self): ...
    @classmethod
    def __subclasshook__(cls, C): ...
    __class_getitem__: Incomplete

class Iterator(Iterable, metaclass=abc.ABCMeta):
    @abstractmethod
    def __next__(self): ...
    def __iter__(self): ...
    @classmethod
    def __subclasshook__(cls, C): ...

class Reversible(Iterable, metaclass=abc.ABCMeta):
    @abstractmethod
    def __reversed__(self): ...
    @classmethod
    def __subclasshook__(cls, C): ...

class Generator(Iterator, metaclass=abc.ABCMeta):
    def __next__(self): ...
    @abstractmethod
    def send(self, value): ...
    @abstractmethod
    def throw(self, typ, val: Incomplete | None = None, tb: Incomplete | None = None): ...
    def close(self) -> None: ...
    @classmethod
    def __subclasshook__(cls, C): ...

class Sized(metaclass=ABCMeta):
    @abstractmethod
    def __len__(self): ...
    @classmethod
    def __subclasshook__(cls, C): ...

class Container(metaclass=ABCMeta):
    @abstractmethod
    def __contains__(self, x): ...
    @classmethod
    def __subclasshook__(cls, C): ...
    __class_getitem__: Incomplete

class Collection(Sized, Iterable, Container, metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, C): ...

class Buffer(metaclass=ABCMeta):
    @abstractmethod
    def __buffer__(self, flags: int, /) -> memoryview: ...
    @classmethod
    def __subclasshook__(cls, C): ...

class _CallableGenericAlias(GenericAlias):
    def __new__(cls, origin, args): ...
    def __reduce__(self): ...
    def __getitem__(self, item): ...

class Callable(metaclass=ABCMeta):
    @abstractmethod
    def __call__(self, *args, **kwds): ...
    @classmethod
    def __subclasshook__(cls, C): ...
    __class_getitem__: Incomplete

class Set(Collection, metaclass=abc.ABCMeta):
    def __le__(self, other): ...
    def __lt__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
    def __eq__(self, other): ...
    def __and__(self, other): ...
    __rand__ = __and__
    def isdisjoint(self, other): ...
    def __or__(self, other): ...
    __ror__ = __or__
    def __sub__(self, other): ...
    def __rsub__(self, other): ...
    def __xor__(self, other): ...
    __rxor__ = __xor__

class MutableSet(Set, metaclass=abc.ABCMeta):
    @abstractmethod
    def add(self, value): ...
    @abstractmethod
    def discard(self, value): ...
    def remove(self, value) -> None: ...
    def pop(self): ...
    def clear(self) -> None: ...
    def __ior__(self, it): ...
    def __iand__(self, it): ...
    def __ixor__(self, it): ...
    def __isub__(self, it): ...

class Mapping(Collection, metaclass=abc.ABCMeta):
    __abc_tpflags__: Incomplete
    @abstractmethod
    def __getitem__(self, key): ...
    def get(self, key, default: Incomplete | None = None): ...
    def __contains__(self, key) -> bool: ...
    def keys(self): ...
    def items(self): ...
    def values(self): ...
    def __eq__(self, other): ...
    __reversed__: Incomplete

class MappingView(Sized):
    def __init__(self, mapping) -> None: ...
    def __len__(self) -> int: ...
    __class_getitem__: Incomplete

class KeysView(MappingView, Set):
    def __contains__(self, key) -> bool: ...
    def __iter__(self): ...

class ItemsView(MappingView, Set):
    def __contains__(self, item) -> bool: ...
    def __iter__(self): ...

class ValuesView(MappingView, Collection):
    def __contains__(self, value) -> bool: ...
    def __iter__(self): ...

class MutableMapping(Mapping, metaclass=abc.ABCMeta):
    @abstractmethod
    def __setitem__(self, key, value): ...
    @abstractmethod
    def __delitem__(self, key): ...
    def pop(self, key, default=...): ...
    def popitem(self): ...
    def clear(self) -> None: ...
    def update(self, other=(), /, **kwds) -> None: ...
    def setdefault(self, key, default: Incomplete | None = None): ...

class Sequence(Reversible, Collection, metaclass=abc.ABCMeta):
    __abc_tpflags__: Incomplete
    @abstractmethod
    def __getitem__(self, index): ...
    def __iter__(self): ...
    def __contains__(self, value) -> bool: ...
    def __reversed__(self) -> _Generator[Incomplete]: ...
    def index(self, value, start: int = 0, stop: Incomplete | None = None): ...
    def count(self, value): ...

class _DeprecateByteStringMeta(ABCMeta):
    def __new__(cls, name, bases, namespace, **kwargs): ...
    def __instancecheck__(cls, instance): ...

class ByteString(Sequence, metaclass=_DeprecateByteStringMeta): ...

class MutableSequence(Sequence, metaclass=abc.ABCMeta):
    @abstractmethod
    def __setitem__(self, index, value): ...
    @abstractmethod
    def __delitem__(self, index): ...
    @abstractmethod
    def insert(self, index, value): ...
    def append(self, value) -> None: ...
    def clear(self) -> None: ...
    def reverse(self) -> None: ...
    def extend(self, values) -> None: ...
    def pop(self, index: int = -1): ...
    def remove(self, value) -> None: ...
    def __iadd__(self, values): ...