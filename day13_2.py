import utils


def do_instruction(
    points: set[tuple[int, int]], axis: str, coordinate: int
) -> set[tuple[int, int]]:
    result = set()
    for x, y in points:
        if axis == "x":
            result.add((x, y) if x <= coordinate else ((coordinate) * 2 - x, y))
        else:
            result.add((x, y) if y <= coordinate else (x, (coordinate) * 2 - y))
    return result


def print_dots(points: set[tuple[int, int]]) -> None:
    assert min([x for x, y in points]) >= 0
    assert min([y for x, y in points]) >= 0
    max_x = max([x for x, y in points])
    max_y = max([y for x, y in points])
    for y in range(max_y+1):
        print("".join(["#" if (x, y) in points else "." for x in range(max_x+1)]))
    print("")


def main():
    points = set()
    instructions = []
    with utils.open_input_file(day=13, example=False) as stdin:
        while True:
            tokens = [*utils.read_tokens(stdin, int, separator="[ \n,]+")]
            if not tokens:
                break
            points.add((tokens[0], tokens[1]))
        while True:
            tokens = [*utils.read_tokens(stdin, str, separator="[ \n=]+")]
            if not tokens:
                break
            instructions.append((tokens[2], int(tokens[3])))
    for instruction in instructions:
        points = do_instruction(points, axis=instruction[0], coordinate=instruction[1])
    print_dots(points)

main()
