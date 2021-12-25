import utils


def calc(add_x: list[int], add_y: list[int], results: list[int], step: int = 0, result: int = 0, z: int = 0) -> None:
    if step == 14:
        if z == 0:
            results.append(result)
        return

    if add_x[step] > 0:
        for digit in range(1, 10):
            calc(add_x, add_y, results, step + 1, result * 10 + digit, z * 26 + add_y[step] + digit)
    else:
        digit = z % 26 + add_x[step]
        if digit not in range(1, 10):
            return
        calc(add_x, add_y, results, step + 1, result * 10 + digit, z // 26)


def main():
    with utils.open_input_file(day=24, example=False) as stdin:
        commands = []
        while True:
            tokens = [*utils.read_tokens(stdin, str)]
            if not tokens:
                break
            commands.append(tokens)
    blocks = []
    block = []
    for command in commands:
        if command[0] == "inp":
            if block:
                blocks.append(block)
            block = []
        block.append(command)
    blocks.append(block)
    assert len(blocks) == 14

    add_x = []
    add_y = []
    for block in blocks:
        add_x.append(int(block[5][2]))
        add_y.append(int(block[15][2]))

    results = []
    calc(add_x, add_y, results)
    results = sorted(results)
    print(results[0])
    print(results[-1])


main()
