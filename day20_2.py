import utils


def value(field: list[str], i: int, j: int) -> str:
    if i < 0:
        i = 0
    if i >= len(field):
        i = len(field) - 1
    if j < 0:
        j = 0
    if j >= len(field[0]):
        j = len(field[0]) - 1
    return field[i][j]


def print_field(field: list[str]) -> None:
    for line in field:
        print(line)
    print()


BORDER = 60

def main():
    with utils.open_input_file(day=20, example=False) as stdin:
        [enhancement_algorithm] = [*utils.read_tokens(stdin, str)]
        stdin.readline()
        field = []
        while True:
            tokens = [*utils.read_tokens(stdin, str)]
            if not tokens:
                break
            field.append(tokens[0])
        h = len(field)
        w = len(field[0])
        field = [("." * BORDER) + line + ("." * BORDER) for line in field]
        w += BORDER*2
        for i in range(BORDER):
            field.insert(0, "." * w)
            field.append("." * w)
        h += BORDER*2

    for iteration in range(50):
        print(f"Iteration {iteration}")
        new_field = []
        for i in range(h):
            new_field_line = ""
            for j in range(w):
                code = ""
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        code += value(field, i + x, j + y)
                code = code.replace(".", "0").replace("#", "1")
                int_code = int(code, 2)
                new_field_line += enhancement_algorithm[int_code]
            new_field.append(new_field_line)
        field = new_field

    result = 0
    for i in range(h):
        for j in range(w):
            if field[i][j] == "#":
                result += 1
    print(result)



main()
