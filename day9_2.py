import utils


def main():
    with utils.open_input_file(day=9) as stdin:
        lines = []
        while True:
            line = stdin.readline().strip("\n")
            if not line:
                break
            lines.append(line)
        field = [
            [9] * (len(lines[0]) + 2),
            *[[9, *[ord(x) - ord("0") for x in line], 9] for line in lines],
            [9] * (len(lines[0]) + 2),
        ]

    def dfs(i: int, j: int, value: int) -> int:
        result = 1
        field[i][j] = value
        for i1, j1 in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
            if field[i1][j1] in range(0, 9):
                result += dfs(i1, j1, value)
        return result

    basins = []
    for i in range(1, len(field) - 1):
        for j in range(1, len(field[0]) - 1):
            if field[i][j] in range(0, 9):
                basins.append(dfs(i, j, -1))
    a, b, c = sorted(basins)[-3:]
    print(a * b * c)


main()
