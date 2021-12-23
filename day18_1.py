import abc

import utils


class Number(abc.ABC):
    @abc.abstractmethod
    def append_left(self, delta: int) -> "Number":
        ...

    @abc.abstractmethod
    def append_right(self, delta: int) -> "Number":
        ...

    @abc.abstractmethod
    def magnitude(self) -> int:
        ...

    @abc.abstractmethod
    def __str__(self) -> str:
        ...

    def __eq__(self, other: "Number") -> bool:
        return self.__str__() == other.__str__()


class SingleNumber(Number):
    def __init__(self, value: int):
        self.value = value

    def append_left(self, delta: int) -> Number:
        return SingleNumber(self.value + delta)

    def append_right(self, delta: int) -> Number:
        return SingleNumber(self.value + delta)

    def magnitude(self) -> int:
        return self.value

    def __str__(self) -> str:
        return f"{self.value}"


class PairNumber(Number):
    def __init__(self, left: Number, right: Number):
        self.left = left
        self.right = right

    def append_left(self, delta: int) -> Number:
        return PairNumber(self.left.append_left(delta), self.right)

    def append_right(self, delta: int) -> Number:
        return PairNumber(self.left, self.right.append_right(delta))

    def magnitude(self) -> int:
        return self.left.magnitude() * 3 + self.right.magnitude() * 2

    def __str__(self) -> str:
        return f"[{self.left},{self.right}]"


def parse_number(value: str, position: int = 0) -> tuple[Number, int]:
    if value[position].isdigit():
        result = 0
        while value[position].isdigit():
            result = result * 10 + int(value[position])
            position += 1
        return SingleNumber(result), position
    if value[position] == "[":
        first, position = parse_number(value, position + 1)
        assert value[position] == ","
        second, position = parse_number(value, position + 1)
        assert value[position] == "]"
        position += 1
        return PairNumber(first, second), position
    assert False, value[position]


def normalize_explode(number: Number, height: int = 0) -> tuple[Number, int, int, bool]:
    if isinstance(number, PairNumber):
        if (
            height >= 4
            and isinstance(number.left, SingleNumber)
            and isinstance(number.right, SingleNumber)
        ):
            return SingleNumber(0), number.left.value, number.right.value, True
        left, left_delta, right_delta, normalized = normalize_explode(
            number.left, height + 1
        )
        if normalized:
            right = number.right.append_left(right_delta)
            return PairNumber(left, right), left_delta, 0, True
        right, left_delta, right_delta, normalized = normalize_explode(
            number.right, height + 1
        )
        if normalized:
            left = number.left.append_right(left_delta)
            return PairNumber(left, right), 0, right_delta, True

    return number, 0, 0, False


def normalize_split(number: Number) -> tuple[Number, bool]:
    if isinstance(number, SingleNumber):
        if number.value > 9:
            return (
                PairNumber(
                    SingleNumber(number.value // 2),
                    SingleNumber((number.value // 2) + (number.value % 2)),
                ),
                True,
            )
        return number, False
    if isinstance(number, PairNumber):
        left, normalized = normalize_split(number.left)
        if normalized:
            return PairNumber(left, number.right), True
        right, normalized = normalize_split(number.right)
        if normalized:
            return PairNumber(number.left, right), True
    return number, False


def normalize(number: Number) -> Number:
    result = number
    while True:
        result, _, _, normalized = normalize_explode(result)
        if normalized:
            continue
        result, normalized = normalize_split(result)
        if normalized:
            continue
        break
    return result


def add(left: Number, right: Number) -> Number:
    return PairNumber(left, right)


def main():
    numbers = []
    with utils.open_input_file(day=18, example=False) as stdin:
        while True:
            tokens = [*utils.read_tokens(stdin, str)]
            if not tokens:
                break
            number = tokens[0]
            numbers.append(parse_number(number)[0])
    result = numbers[0]
    for x in numbers[1:]:
        result = normalize(add(result, x))
    print(f"{result.magnitude()}")


main()
