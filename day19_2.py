from typing import Optional

import numpy

import utils


class Matrix:
    def __init__(self, value: list[list[int]]):
        self._rows_count = len(value)
        self._columns_count = len(value[0])
        for row in value:
            assert len(row) == self._columns_count
        self._value = value

    @staticmethod
    def empty(rows_count: int, columns_count: int) -> "Matrix":
        return Matrix([[0] * columns_count for _ in range(rows_count)])

    @staticmethod
    def vector(value: list[int]) -> "Matrix":
        return Matrix([value])

    @property
    def rows_count(self):
        return self._rows_count

    @property
    def columns_count(self):
        return self._columns_count

    @staticmethod
    def from_numpy_array(
        matrix: numpy.array, rows_count: int, columns_count: int
    ) -> "Matrix":
        result = Matrix.empty(rows_count, columns_count)
        for i in range(rows_count):
            for j in range(columns_count):
                result[(i, j)] = matrix[i][j]
        return result

    def to_numpy_array(self) -> numpy.array:
        return numpy.array(self._value)

    def __eq__(self, other: "Matrix") -> bool:
        return numpy.array_equal(self._value, other._value)

    def __mul__(self, other: "Matrix"):
        assert self.columns_count == other.rows_count
        result = numpy.matmul(self.to_numpy_array(), other.to_numpy_array())
        return Matrix.from_numpy_array(result, self.rows_count, other.columns_count)

    def __sub__(self, other: "Matrix") -> "Matrix":
        assert self.rows_count == other.rows_count
        assert self.columns_count == other.columns_count
        return Matrix.from_numpy_array(
            numpy.subtract(self.to_numpy_array(), other.to_numpy_array()),
            self.rows_count,
            self.columns_count,
        )

    def __add__(self, other):
        assert self.rows_count == other.rows_count
        assert self.columns_count == other.columns_count
        return Matrix.from_numpy_array(
            numpy.add(self.to_numpy_array(), other.to_numpy_array()),
            self.rows_count,
            self.columns_count,
        )

    def __getitem__(self, key: tuple[int, int]) -> int:
        i, j = key
        assert i in range(0, self.rows_count)
        assert j in range(0, self.columns_count)
        return self._value[i][j]

    def __setitem__(self, key: tuple[int, int], value: int) -> None:
        i, j = key
        assert i in range(0, self.rows_count)
        assert j in range(0, self.columns_count)
        self._value[i][j] = value

    def __str__(self):
        return str(self.to_numpy_array())

    def __hash__(self) -> int:
        result = 0
        for i in range(self.rows_count):
            for j in range(self.columns_count):
                result = (result * 3 + self[(i, j)]) & (2 ** 32 - 1)
        return hash(result)


Vector = tuple[int, int, int]

rotations = [
    Matrix([[1, 0, 0], [0, 0, -1], [0, 1, 0]]),
    Matrix([[0, 0, -1], [0, 1, 0], [1, 0, 0]]),
]


def build_all_rotations():
    while True:
        new_rotations = []
        for r1 in rotations:
            for r2 in rotations:
                candidate = r1 * r2
                if candidate not in rotations:
                    if candidate not in new_rotations:
                        new_rotations.append(candidate)
        if not new_rotations:
            break
        rotations.extend(new_rotations)


def rotate(vector: Vector, rotation: Matrix) -> Vector:
    return (
        vector[0] * rotation[(0, 0)]
        + vector[1] * rotation[(0, 1)]
        + vector[2] * rotation[(0, 2)],
        vector[0] * rotation[(1, 0)]
        + vector[1] * rotation[(1, 1)]
        + vector[2] * rotation[(1, 2)],
        vector[0] * rotation[(2, 0)]
        + vector[1] * rotation[(2, 1)]
        + vector[2] * rotation[(2, 2)],
    )


def find_match(
    beacons1: list[Vector], beacons2: list[Vector]
) -> Optional[tuple[Matrix, Vector]]:
    list1 = {x for x in beacons1}
    for rotation in rotations:
        list2 = {rotate(x, rotation) for x in beacons2}
        for x in list1:
            for y in list2:
                delta = subtract_vectors(x, y)
                list2_ = {sum_vectors(z, delta) for z in list2}
                if len(list1.intersection(list2_)) >= 12:
                    return rotation, delta
    return None


def sum_vectors(a: Vector, b: Vector) -> Vector:
    return a[0] + b[0], a[1] + b[1], a[2] + b[2]


def subtract_vectors(a: Vector, b: Vector) -> Vector:
    return a[0] - b[0], a[1] - b[1], a[2] - b[2]


def distance(a: Vector, b: Vector) -> Vector:
    res = subtract_vectors(a, b)
    return abs(res[0]) + abs(res[1]) + abs(res[2])


def main():
    scanners = []
    build_all_rotations()
    with utils.open_input_file(day=19, example=False) as stdin:
        while True:
            tokens = [*utils.read_tokens(stdin, int, r"[^\d]+")]
            if not tokens:
                break
            beacons = []
            while True:
                tokens = [*utils.read_tokens(stdin, int, r"[ ,\n]+")]
                if not tokens:
                    break
                assert len(tokens) == 3
                beacons.append((tokens[0], tokens[1], tokens[2]))
            scanners.append(beacons)

    processed: list[bool] = [False] * len(scanners)
    processed[0] = True
    queue = [0]
    l = 0
    scanner_position = [(0, 0, 0)] * len(scanners)
    while l < len(queue):
        current = queue[l]
        l += 1
        for i in range(len(scanners)):
            if not processed[i]:
                print(f"find match start {current} {i}")
                match = find_match(scanners[current], scanners[i])
                print(f"find match end {current} {i} {match is not None}")
                if match:
                    scanners[i] = [
                        sum_vectors(rotate(beacon, match[0]), match[1])
                        for beacon in scanners[i]
                    ]
                    scanner_position[i] = sum_vectors(
                        rotate(scanner_position[0], match[0]), match[1]
                    )
                    queue.append(i)
                    processed[i] = True
                    print(len(queue))

    result = set()
    for i in range(len(scanners)):
        for beacon in scanners[i]:
            result.add(beacon)

    max_result = 0
    for scanner1 in scanner_position:
        for scanner2 in scanner_position:
            candidate = distance(scanner1, scanner2)
            if max_result < candidate:
                max_result = candidate
    print(max_result)


main()
