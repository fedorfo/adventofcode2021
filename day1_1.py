from typing import Optional

import utils


def main():
    with utils.open_input_file(day=1) as stdin:
        previous: Optional[int] = None
        increments = 0
        while True:
            current = next(utils.read_tokens(stdin, int), None)
            if current is None:
                break
            if previous is not None and current > previous:
                increments += 1
            previous = current
        print(increments)


main()
