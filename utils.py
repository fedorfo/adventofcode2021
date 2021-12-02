import contextlib
from typing import TextIO, Callable, Type, Iterator, Tuple

T = Type["T"]


def read_tokens(input_stream: TextIO, ctor: Callable[[str], T]) -> Iterator[T]:
    return (ctor(x) for x in input_stream.readline().split())


@contextlib.contextmanager
def init_stdin_stdout(input_file: str, output_file: str) -> Iterator[Tuple[TextIO, TextIO]]:
    with open(f"inputs/{input_file}", "r") as input_stream:
        with open(f"inputs/{output_file}", "w") as output_stream:
            yield input_stream, output_stream
