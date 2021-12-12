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
ALL_CHARACTERS = OPENING_CHARACTERS + CLOSING_CHARACTERS

SCORE = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


def process_line(line: str) -> int:
    stack = []
    for i, ch in enumerate(line):
        if ch in OPENING_CHARACTERS:
            stack.append(ch)
        else:
            assert ch in CLOSING_CHARACTERS
            if stack[-1] != OPENING_CHARACTER_BY_CLOSING[ch]:
                return SCORE[ch]
            else:
                stack.pop()
    return 0


def main():
    with utils.open_input_file(day=10) as stdin:
        lines = []
        while True:
            line = stdin.readline().strip("\n")
            if not line:
                break
            lines.append(line)

    result = 0
    for line in lines:
        result += process_line(line)

    print(result)


main()
