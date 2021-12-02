from typing import Optional

import utils


def get_shift(direction: str, length: int):
    if direction == "forward":
        return length, 0
    elif direction == "down":
        return 0, length
    elif direction == "up":
        return 0, -length
    else:
        raise RuntimeError(f"Incorrect direction {direction}")


def main():
    x, y = 0, 0
    with utils.init_stdin_stdout("day2.in", "day2_1.out") as (stdin, stdout):
        while stdin.readable():
            tokens = [*utils.read_tokens(stdin, str)]
            if not tokens:
                break
            x1, y1 = get_shift(tokens[0], int(tokens[1]))
            x, y = x + x1, y + y1

        stdout.write(f"{x*y}")


main()
