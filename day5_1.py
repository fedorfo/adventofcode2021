import utils


def sign(x: int) -> int:
    return 1 if x > 0 else (-1 if x < 0 else 0)


class Point:
    __slots__ = (
        "x",
        "y",
    )

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Point") -> "Point":
        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, other: "Point"):
        return self.x == other.x and self.y == other.y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def normalize(self) -> "Point":
        return Point(sign(self.x), sign(self.y))


def main():
    with utils.open_input_file(day=5) as stdin:
        segments = []

        while True:
            numbers = [*utils.read_tokens(stdin, int, r"[,\-> \n]+")]
            if not numbers:
                break
            segments.append(
                (Point(numbers[0], numbers[1]), Point(numbers[2], numbers[3]))
            )

    min_x = min(min(segment[0].x, segment[1].x) for segment in segments)
    min_y = min(min(segment[0].y, segment[1].y) for segment in segments)
    max_x = max(max(segment[0].x, segment[1].x) for segment in segments)
    max_y = max(max(segment[0].y, segment[1].y) for segment in segments)
    assert min_x >= 0
    assert min_y >= 0
    field = [[0] * (max_y + 1) for _ in range(max_x + 1)]

    for segment in segments:
        direction = (segment[1] - segment[0]).normalize()
        if 0 not in (direction.x, direction.y):
            continue

        p = segment[0]
        while True:
            field[p.x][p.y] = field[p.x][p.y] + 1
            if p == segment[1]:
                break
            p = p + direction

    result = 0
    for x in range(max_x + 1):
        for y in range(max_y + 1):
            if field[x][y] >= 2:
                result += 1

    print(result)


main()
