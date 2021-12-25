import utils


def empty_field(h: int, w: int) -> list[list[str]]:
    new_field = [["." for _ in range(w)] for _ in range(h)]
    return new_field


def main():
    field = []
    with utils.open_input_file(day=25, example=False) as stdin:
        while True:
            line = stdin.readline().strip()
            if not line:
                break
            field.append([x for x in line])

    steps = 0
    h = len(field)
    w = len(field[0])
    while True:
        print(f"Step #{steps}.")
        for line in field:
            print("".join(line))
        print()

        moves = 0
        new_field = empty_field(h, w)
        for i in range(h):
            for j in range(w):
                if field[i][j] == "v":
                    new_field[i][j] = "v"
                if field[i][j] == ">":
                    if field[i][(j + 1) % w] == ".":
                        new_field[i][j] = "."
                        new_field[i][(j + 1) % w] = ">"
                        moves += 1
                    else:
                        new_field[i][j] = ">"

        field = new_field
        new_field = empty_field(h, w)
        for i in range(h):
            for j in range(w):
                if field[i][j] == "v":
                    if field[(i + 1) % h][j] == ".":
                        new_field[i][j] = "."
                        new_field[(i + 1) % h][j] = "v"
                        moves += 1
                    else:
                        new_field[i][j] = "v"
                if field[i][j] == ">":
                    new_field[i][j] = ">"
        field = new_field

        if moves == 0:
            break

        steps += 1

    print(steps+1)


main()
