import contextlib
import re
from typing import TextIO, Callable, Type, Iterator, Optional, Union

T = Type["T"]


def read_tokens(
    input_stream: TextIO,
    ctor: Optional[Callable[[str], T]] = None,
    separator: Union[str] = "[ \n]+",
) -> Iterator[T]:
    line = input_stream.readline()
    tokens = re.split(separator, line)
    tokens = [x for x in tokens if x]
    return (ctor(x) if ctor is not None else x for x in tokens)


@contextlib.contextmanager
def open_input_file(*, day: int, example: bool = False) -> Iterator[TextIO]:
    with open(
        f"inputs/day{day}{'_example' if example else ''}.in", "r"
    ) as input_stream:
        yield input_stream
