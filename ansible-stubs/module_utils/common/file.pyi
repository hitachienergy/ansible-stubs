from _typeshed import Incomplete

__metaclass__ = type
HAVE_SELINUX: bool
FILE_ATTRIBUTES: Incomplete
MODE_OPERATOR_RE: Incomplete
USERS_RE: Incomplete
PERMS_RE: Incomplete

def is_executable(path): ...
def format_attributes(attributes): ...
def get_flags_from_attributes(attributes): ...
def get_file_arg_spec(): ...
