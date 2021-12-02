from typing import Optional

import utils


def main():
    with utils.init_stdin_stdout("day1.in", "day1_1.out") as (stdin, stdout):
        previous: Optional[int] = None
        increments = 0
        while stdin.readable():
            current = next(utils.read_tokens(stdin, int), None)
            if current is None:
                break
            if previous is not None and current > previous:
                increments += 1
            previous = current
        stdout.write(f"{increments}")


main()
