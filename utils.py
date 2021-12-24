import contextlib
import re
from typing import TextIO, Callable, Type, Iterator, Optional, Union

T = Type["T"]


def split_to_tokens(
    value: str,
    ctor: Optional[Callable[[str], T]] = None,
    separator: Union[str] = "[ \n]+",
) -> Iterator[T]:
    tokens = re.split(separator, value)
    tokens = [x for x in tokens if x]
    return (ctor(x) if ctor is not None else x for x in tokens)


def read_tokens(
    input_stream: TextIO,
    ctor: Optional[Callable[[str], T]] = None,
    separator: Union[str] = "[ \n]+",
) -> Iterator[T]:
    line = input_stream.readline()
    return split_to_tokens(line, ctor, separator)


@contextlib.contextmanager
def open_input_file(*, day: int, example: bool = False) -> Iterator[TextIO]:
    with open(f"inputs/day{day}{'_example' if example else ''}.in", "r") as input_stream:
        yield input_stream
