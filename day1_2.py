from typing import Optional

import utils


def main():
    with utils.init_stdin_stdout("day1.in", "day1_2.out") as (stdin, stdout):
        previous_list: list[int] = []
        increments = 0
        while stdin.readable():
            current = next(utils.read_tokens(stdin, int), None)
            if current is None:
                break
            if len(previous_list) == 3:
                current_list = [*previous_list[1:], current]
                if sum(current_list) > sum(previous_list):
                    increments += 1
                previous_list = current_list
            else:
                previous_list.append(current)
        stdout.write(f"{increments}")


main()
