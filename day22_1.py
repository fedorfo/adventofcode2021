import utils


def main():
    with utils.open_input_file(day=22, example=False) as stdin:
        commands = []
        while True:
            line: str = stdin.readline()
            tokens = line.split(" ", maxsplit=1)
            if len(tokens) < 2:
                break
            action = tokens[0]
            tokens = [*utils.split_to_tokens(tokens[1], int, r"[^\d-]+")]
            if not tokens:
                break
            commands.append([action == "on", *tokens])
    reactor = [[[False] * 101 for _ in range(-50, 51)] for _ in range(-50, 51)]

    for command in commands:
        x1 = max(command[1], -50)
        x2 = min(command[2], 50)
        y1 = max(command[3], -50)
        y2 = min(command[4], 50)
        z1 = max(command[5], -50)
        z2 = min(command[6], 50)
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                for z in range(z1, z2 + 1):
                    reactor[x][y][z] = command[0]

    result = 0
    for x in range(-50, 51):
        for y in range(-50, 51):
            for z in range(-50, 51):
                if reactor[x][y][z]:
                    result += 1
    print(result)


main()
