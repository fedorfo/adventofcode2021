import utils

CHARACTER_PAIRS = [
    ("(", ")"),
    ("[", "]"),
    ("{", "}"),
    ("<", ">"),
]
OPENING_CHARACTERS = [x[0] for x in CHARACTER_PAIRS]
CLOSING_CHARACTERS = [x[1] for x in CHARACTER_PAIRS]
OPENING_CHARACTER_BY_CLOSING = {x[1]: x[0] for x in CHARACTER_PAIRS}
CLOSING_CHARACTER_BY_OPENING = {x[0]: x[1] for x in CHARACTER_PAIRS}
ALL_CHARACTERS = OPENING_CHARACTERS + CLOSING_CHARACTERS

SCORE = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def process_line(line: str) -> int:
    stack = []
    for i, ch in enumerate(line):
        if ch in OPENING_CHARACTERS:
            stack.append(ch)
        else:
            assert ch in CLOSING_CHARACTERS
            if stack[-1] != OPENING_CHARACTER_BY_CLOSING[ch]:
                return 0
            else:
                stack.pop()
    result = 0
    for x in stack[::-1]:
        result = result * 5 + SCORE[CLOSING_CHARACTER_BY_OPENING[x]]
    return result


def main():
    with utils.open_input_file(day=10) as stdin:
        lines = []
        while True:
            line = stdin.readline().strip("\n")
            if not line:
                break
            lines.append(line)

    results = []
    for line in lines:
        result = process_line(line)
        if result != 0:
            results.append(result)
    results.sort()

    print(results[(len(results)-1) // 2])


main()
