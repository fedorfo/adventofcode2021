import utils


def print_field(field: list[list[int]]) -> None:
    for line in field:
        print("".join((str(x) for x in line)))


def make_iteration(field: list[list[int]]) -> int:
    def dfs(x: int, y: int) -> None:
        field[x][y] += 1
        if field[x][y] == 10:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    if x + i not in range(len(field)) or y + j not in range(
                        len(field[0])
                    ):
                        continue
                    dfs(x + i, y + j)

    for x in range(len(field)):
        for y in range(len(field[0])):
            dfs(x, y)

    highlights = 0
    for x in range(len(field)):
        for y in range(len(field[0])):
            if field[x][y] > 9:
                field[x][y] = 0
                highlights += 1
    return highlights


def main():
    with utils.open_input_file(day=11) as stdin:
        lines = []
        while True:
            line = stdin.readline().strip("\n")
            if not line:
                break
            lines.append(line)

    field = [[ord(ch) - ord("0") for ch in line] for line in lines]
    result = 0

    for i in range(100):
        result += make_iteration(field)
    print(result)


main()
