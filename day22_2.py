import numpy

import utils


def get_real_coordinates(coordinates_list: list[int], index: int) -> tuple[int, int]:
    if index % 2 == 0:
        result = coordinates_list[index // 2]
        return result, result
    left = coordinates_list[index // 2] + 1
    right = coordinates_list[(index + 1) // 2] - 1
    return left, right


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

    x_values, y_values, z_values = set(), set(), set()
    for command in commands:
        x_values.add(command[1])
        x_values.add(command[2])
        y_values.add(command[3])
        y_values.add(command[4])
        z_values.add(command[5])
        z_values.add(command[6])
    x_values_list = sorted(list(x_values))
    y_values_list = sorted(list(y_values))
    z_values_list = sorted(list(z_values))

    print("create reactor array")
    reactor = numpy.zeros(
        [
            len(x_values_list) * 2 - 1,
            len(y_values_list) * 2 - 1,
            len(z_values_list) * 2 - 1,
        ]
    )
    # reactor = numpy.array(
    #     [False] * (len(x_values_list) * 2 - 1) * (len(y_values_list) * 2 - 1) * (len(z_values_list) * 2 - 1)
    # ).reshape(
    #     [
    #         len(x_values_list) * 2 - 1,
    #         len(y_values_list) * 2 - 1,
    #         len(z_values_list) * 2 - 1,
    #     ]
    # )

    for i, command in enumerate(commands):
        print(f"Process command {i+1}/{len(commands)}")
        x1 = x_values_list.index(command[1]) * 2
        x2 = x_values_list.index(command[2]) * 2
        y1 = y_values_list.index(command[3]) * 2
        y2 = y_values_list.index(command[4]) * 2
        z1 = z_values_list.index(command[5]) * 2
        z2 = z_values_list.index(command[6]) * 2
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                for z in range(z1, z2 + 1):
                    reactor[x][y][z] = command[0]

    print("")
    result = 0
    for i, x in enumerate(range(len(x_values_list) * 2 - 1)):
        print(f"Calculate result {x}/{len(x_values_list) * 2 - 1}")
        x1, x2 = get_real_coordinates(x_values_list, x)
        if x1 > x2:
            continue
        for y in range(len(y_values_list) * 2 - 1):
            y1, y2 = get_real_coordinates(y_values_list, y)
            if y1 > y2:
                continue
            for z in range(len(z_values_list) * 2 - 1):
                z1, z2 = get_real_coordinates(z_values_list, z)
                if z1 > z2:
                    continue

                if reactor[x][y][z]:
                    result += (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)
    print(result)


main()
