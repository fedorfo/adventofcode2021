import utils


def extend_field(field: list[list[int]]) -> list[list[int]]:
    h, w = len(field), len(field[0])
    new_field = [[0] * w * 5 for _ in range(h * 5)]
    for i in range(h * 5):
        for j in range(w * 5):
            value = (field[i % h][j % w] + i // h + j // w) % 9
            if value == 0:
                value = 9
            new_field[i][j] = value
    return new_field


def read_field() -> list[list[int]]:
    with utils.open_input_file(day=15, example=False) as stdin:
        lines = []
        while True:
            line = stdin.readline().strip("\n")
            if not line:
                break
            lines.append(line)
    result = [[ord(ch) - ord("0") for ch in line] for line in lines]
    return extend_field(result)


def main():
    field = read_field()
    h, w = len(field), len(field[0])
    dist: list[list[int]] = [[10 ** 9] * w for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    dist[0][0] = 0
    min_values: list[list[tuple[int, int]]] = [[] for _ in range(w * h * 9 + 1)]
    min_values[0].append((0, 0))
    for min_value in range(len(min_values)):
        for i0, j0 in min_values[min_value]:
            if dist[i0][j0] < min_value:
                continue

            visited[i0][j0] = True
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    if (abs(di) + abs(dj)) != 1:
                        continue
                    i1, j1 = i0 + di, j0 + dj
                    if i1 not in range(0, h) or j1 not in range(0, w):
                        continue
                    new_dist = dist[i0][j0] + field[i1][j1]
                    if dist[i1][j1] > new_dist:
                        dist[i1][j1] = new_dist
                        min_values[new_dist].append((i1, j1))

    print(dist[h - 1][w - 1])


main()
