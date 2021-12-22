from collections import defaultdict

import utils


def read_field() -> list[list[int]]:
    with utils.open_input_file(day=15, example=False) as stdin:
        lines = []
        while True:
            line = stdin.readline().strip("\n")
            if not line:
                break
            lines.append(line)
    return [[ord(ch) - ord("0") for ch in line] for line in lines]


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
