from typing import Optional

import utils


def get_shift(current_aim: int, direction: str, length: int) -> tuple[int, int, int]:
    if direction == "forward":
        return length, current_aim*length, 0
    elif direction == "down":
        return 0, 0, length
    elif direction == "up":
        return 0, 0, -length
    else:
        raise RuntimeError(f"Incorrect direction {direction}")


def main():
    x, y, aim = 0, 0, 0
    with utils.init_stdin_stdout("day2.in", "day2_2.out") as (stdin, stdout):
        while stdin.readable():
            tokens = [*utils.read_tokens(stdin, str)]
            if not tokens:
                break
            x1, y1, aim1 = get_shift(aim, tokens[0], int(tokens[1]))
            x, y, aim = x + x1, y + y1, aim+aim1

        stdout.write(f"{x*y}")


main()
