import utils


def get_shift(current_aim: int, direction: str, length: int) -> tuple[int, int, int]:
    if direction == "forward":
        return length, current_aim * length, 0
    elif direction == "down":
        return 0, 0, length
    elif direction == "up":
        return 0, 0, -length
    else:
        raise RuntimeError(f"Incorrect direction {direction}")


def main():
    x, y, aim = 0, 0, 0
    with utils.open_input_file(day=2) as stdin:
        while stdin.readable():
            tokens = [*utils.read_tokens(stdin, str)]
            if not tokens:
                break
            x1, y1, aim1 = get_shift(aim, tokens[0], int(tokens[1]))
            x, y, aim = x + x1, y + y1, aim + aim1

        print(x * y)


main()
