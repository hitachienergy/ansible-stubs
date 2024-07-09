import functools
import io
import types
from _typeshed import Incomplete

__version__: str
PY2: Incomplete
PY3: Incomplete
PY34: Incomplete
string_types: Incomplete
integer_types: Incomplete
class_types: Incomplete
text_type = str
binary_type = bytes
MAXSIZE: Incomplete

class _LazyDescr:
    name: Incomplete
    def __init__(self, name) -> None: ...
    def __get__(self, obj, tp): ...

class MovedModule(_LazyDescr):
    mod: Incomplete
    def __init__(self, name, old, new: Incomplete | None = None) -> None: ...
    def __getattr__(self, attr): ...

class _LazyModule(types.ModuleType):
    __doc__: Incomplete
    def __init__(self, name) -> None: ...
    def __dir__(self): ...

class MovedAttribute(_LazyDescr):
    mod: Incomplete
    attr: Incomplete
    def __init__(self, name, old_mod, new_mod, old_attr: Incomplete | None = None, new_attr: Incomplete | None = None) -> None: ...

class _SixMetaPathImporter:
    name: Incomplete
    known_modules: Incomplete
    def __init__(self, six_module_name) -> None: ...
    def find_module(self, fullname, path: Incomplete | None = None): ...
    def find_spec(self, fullname, path, target: Incomplete | None = None): ...
    def load_module(self, fullname): ...
    def is_package(self, fullname): ...
    def get_code(self, fullname) -> None: ...
    get_source = get_code
    def create_module(self, spec): ...
    def exec_module(self, module) -> None: ...

class _MovedItems(_LazyModule): ...

moves: Incomplete

class Module_six_moves_urllib_parse(_LazyModule): ...
class Module_six_moves_urllib_error(_LazyModule): ...
class Module_six_moves_urllib_request(_LazyModule): ...
class Module_six_moves_urllib_response(_LazyModule): ...
class Module_six_moves_urllib_robotparser(_LazyModule): ...

class Module_six_moves_urllib(types.ModuleType):
    parse: Incomplete
    error: Incomplete
    request: Incomplete
    response: Incomplete
    robotparser: Incomplete
    def __dir__(self): ...

def add_move(move) -> None: ...
def remove_move(name) -> None: ...
advance_iterator = next
next = advance_iterator
callable = callable

def get_unbound_function(unbound): ...
create_bound_method = types.MethodType

def create_unbound_method(func, cls): ...
Iterator = object
get_method_function: Incomplete
get_method_self: Incomplete
get_function_closure: Incomplete
get_function_code: Incomplete
get_function_defaults: Incomplete
get_function_globals: Incomplete

def iterkeys(d, **kw): ...
def itervalues(d, **kw): ...
def iteritems(d, **kw): ...
def iterlists(d, **kw): ...

viewkeys: Incomplete
viewvalues: Incomplete
viewitems: Incomplete

def b(s): ...
def u(s): ...
unichr = chr
int2byte: Incomplete
byte2int: Incomplete
indexbytes: Incomplete
iterbytes = iter
StringIO = io.StringIO
BytesIO = io.BytesIO

def assertCountEqual(self, *args, **kwargs): ...
def assertRaisesRegex(self, *args, **kwargs): ...
def assertRegex(self, *args, **kwargs): ...
def assertNotRegex(self, *args, **kwargs): ...

exec_: Incomplete

def reraise(tp, value, tb: Incomplete | None = None) -> None: ...

print_: Incomplete
wraps = functools.wraps

def with_metaclass(meta, *bases): ...
def add_metaclass(metaclass): ...
def ensure_binary(s, encoding: str = 'utf-8', errors: str = 'strict'): ...
def ensure_str(s, encoding: str = 'utf-8', errors: str = 'strict'): ...
def ensure_text(s, encoding: str = 'utf-8', errors: str = 'strict'): ...
def python_2_unicode_compatible(klass): ...
