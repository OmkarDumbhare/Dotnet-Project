from collections.abc import Iterable, Iterator, Sequence
from typing import Any

from pygments.token import _TokenType
from pygments.util import Future

class LexerMeta(type):
    def __new__(cls, name, bases, d): ...
    def analyse_text(self, text) -> None: ...  # actually defined in class Lexer
    # ClassVars of Lexer, but same situation as with StyleMeta and Style
    name: str
    aliases: Sequence[str]  # not intended mutable
    filenames: Sequence[str]
    alias_filenames: Sequence[str]
    mimetypes: Sequence[str]
    priority: int

class Lexer(metaclass=LexerMeta):
    options: Any
    stripnl: Any
    stripall: Any
    ensurenl: Any
    tabsize: Any
    encoding: Any
    filters: Any
    def __init__(self, **options) -> None: ...
    def add_filter(self, filter_, **options) -> None: ...
    def get_tokens(self, text: str, unfiltered: bool = ...) -> Iterator[tuple[_TokenType, str]]: ...
    def get_tokens_unprocessed(self, text: str) -> Iterator[tuple[int, _TokenType, str]]: ...

class DelegatingLexer(Lexer):
    root_lexer: Any
    language_lexer: Any
    needle: Any
    def __init__(self, _root_lexer, _language_lexer, _needle=..., **options) -> None: ...
    def get_tokens_unprocessed(self, text: str) -> Iterator[tuple[int, _TokenType, str]]: ...

class include(str): ...
class _inherit: ...

inherit: Any

class combined(tuple[Any]):
    def __new__(cls, *args): ...
    def __init__(self, *args) -> None: ...

class _PseudoMatch:
    def __init__(self, start, text) -> None: ...
    def start(self, arg: Any | None = ...): ...
    def end(self, arg: Any | None = ...): ...
    def group(self, arg: Any | None = ...): ...
    def groups(self): ...
    def groupdict(self): ...

def bygroups(*args): ...

class _This: ...

this: Any

def using(_other, **kwargs): ...

class default:
    state: Any
    def __init__(self, state) -> None: ...

class words(Future):
    words: Any
    prefix: Any
    suffix: Any
    def __init__(self, words, prefix: str = ..., suffix: str = ...) -> None: ...
    def get(self): ...

class RegexLexerMeta(LexerMeta):
    def process_tokendef(cls, name, tokendefs: Any | None = ...): ...
    def get_tokendefs(cls): ...
    def __call__(cls, *args, **kwds): ...

class RegexLexer(Lexer, metaclass=RegexLexerMeta):
    flags: Any
    tokens: Any
    def get_tokens_unprocessed(self, text: str, stack: Iterable[str] = ...) -> Iterator[tuple[int, _TokenType, str]]: ...

class LexerContext:
    text: Any
    pos: Any
    end: Any
    stack: Any
    def __init__(self, text, pos, stack: Any | None = ..., end: Any | None = ...) -> None: ...

class ExtendedRegexLexer(RegexLexer):
    def get_tokens_unprocessed(  # type: ignore[override]
        self, text: str | None = ..., context: LexerContext | None = ...
    ) -> Iterator[tuple[int, _TokenType, str]]: ...

class ProfilingRegexLexerMeta(RegexLexerMeta): ...

class ProfilingRegexLexer(RegexLexer, metaclass=ProfilingRegexLexerMeta):
    def get_tokens_unprocessed(self, text: str, stack: Iterable[str] = ...) -> Iterator[tuple[int, _TokenType, str]]: ...
