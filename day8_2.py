import itertools

import utils


def sort_chars(value: str) -> str:
    return "".join(sorted([x for x in value]))


digits_map = {
    sort_chars(k): v
    for k, v in {
        "acedgfb": 8,
        "cdfbe": 5,
        "gcdfa": 2,
        "fbcad": 3,
        "dab": 7,
        "cefabd": 9,
        "cdfgeb": 6,
        "eafb": 4,
        "cagedb": 0,
        "ab": 1,
    }.items()
}

digits_set = set(digits_map.keys())

ABC = "abcdefg"


def apply_permutation(digit: str, permutation: str) -> str:
    result = ""
    for x in digit:
        result += permutation[ord(x) - ord("a")]
    return result


def main():
    total_result = 0

    with utils.open_input_file(day=8) as stdin:
        while True:
            puzzle = [*utils.read_tokens(stdin, str, r"[| \n]+")]
            if len(puzzle) == 0:
                break
            result = 0
            for permutation in ["".join(x) for x in itertools.permutations(ABC, 7)]:
                candidate = set(
                    [
                        sort_chars(apply_permutation(digit, permutation))
                        for digit in puzzle[:10]
                    ]
                )
                if candidate == digits_set:
                    result = 0

                    for i, digit in enumerate(puzzle[-4:][::-1]):
                        result += (
                            10 ** i
                            * digits_map[sort_chars(apply_permutation(digit, permutation))]
                        )
                    continue
            assert result != 0
            total_result += result

    print(total_result)


main()
