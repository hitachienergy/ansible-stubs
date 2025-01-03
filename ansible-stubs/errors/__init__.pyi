from _typeshed import Incomplete
from ansible.errors.yaml_strings import YAML_AND_SHORTHAND_ERROR as YAML_AND_SHORTHAND_ERROR, YAML_COMMON_DICT_ERROR as YAML_COMMON_DICT_ERROR, YAML_COMMON_LEADING_TAB_ERROR as YAML_COMMON_LEADING_TAB_ERROR, YAML_COMMON_PARTIALLY_QUOTED_LINE_ERROR as YAML_COMMON_PARTIALLY_QUOTED_LINE_ERROR, YAML_COMMON_UNBALANCED_QUOTES_ERROR as YAML_COMMON_UNBALANCED_QUOTES_ERROR, YAML_COMMON_UNQUOTED_COLON_ERROR as YAML_COMMON_UNQUOTED_COLON_ERROR, YAML_COMMON_UNQUOTED_VARIABLE_ERROR as YAML_COMMON_UNQUOTED_VARIABLE_ERROR, YAML_POSITION_DETAILS as YAML_POSITION_DETAILS
from ansible.module_utils.common.text.converters import to_native as to_native, to_text as to_text

__metaclass__ = type

class AnsibleError(Exception):
    obj: Incomplete
    orig_exc: Incomplete
    def __init__(self, message: str = '', obj: Incomplete | None = None, show_content: bool = True, suppress_extended_error: bool = False, orig_exc: Incomplete | None = None) -> None: ...
    @property
    def message(self): ...
    @message.setter
    def message(self, val) -> None: ...

class AnsiblePromptInterrupt(AnsibleError): ...
class AnsiblePromptNoninteractive(AnsibleError): ...
class AnsibleAssertionError(AnsibleError, AssertionError): ...
class AnsibleOptionsError(AnsibleError): ...
class AnsibleParserError(AnsibleError): ...
class AnsibleInternalError(AnsibleError): ...
class AnsibleRuntimeError(AnsibleError): ...
class AnsibleModuleError(AnsibleRuntimeError): ...
class AnsibleConnectionFailure(AnsibleRuntimeError): ...
class AnsibleAuthenticationFailure(AnsibleConnectionFailure): ...
class AnsibleCallbackError(AnsibleRuntimeError): ...
class AnsibleTemplateError(AnsibleRuntimeError): ...
class AnsibleFilterError(AnsibleTemplateError): ...
class AnsibleLookupError(AnsibleTemplateError): ...
class AnsibleUndefinedVariable(AnsibleTemplateError): ...

class AnsibleFileNotFound(AnsibleRuntimeError):
    file_name: Incomplete
    paths: Incomplete
    def __init__(self, message: str = '', obj: Incomplete | None = None, show_content: bool = True, suppress_extended_error: bool = False, orig_exc: Incomplete | None = None, paths: Incomplete | None = None, file_name: Incomplete | None = None) -> None: ...

class AnsibleAction(AnsibleRuntimeError):
    result: Incomplete
    def __init__(self, message: str = '', obj: Incomplete | None = None, show_content: bool = True, suppress_extended_error: bool = False, orig_exc: Incomplete | None = None, result: Incomplete | None = None) -> None: ...

class AnsibleActionSkip(AnsibleAction):
    def __init__(self, message: str = '', obj: Incomplete | None = None, show_content: bool = True, suppress_extended_error: bool = False, orig_exc: Incomplete | None = None, result: Incomplete | None = None) -> None: ...

class AnsibleActionFail(AnsibleAction):
    def __init__(self, message: str = '', obj: Incomplete | None = None, show_content: bool = True, suppress_extended_error: bool = False, orig_exc: Incomplete | None = None, result: Incomplete | None = None) -> None: ...

class _AnsibleActionDone(AnsibleAction): ...

class AnsiblePluginError(AnsibleError):
    plugin_load_context: Incomplete
    def __init__(self, message: Incomplete | None = None, plugin_load_context: Incomplete | None = None) -> None: ...

class AnsiblePluginRemovedError(AnsiblePluginError): ...
class AnsiblePluginCircularRedirect(AnsiblePluginError): ...
class AnsibleCollectionUnsupportedVersionError(AnsiblePluginError): ...
class AnsibleFilterTypeError(AnsibleTemplateError, TypeError): ...
class AnsiblePluginNotFound(AnsiblePluginError): ...