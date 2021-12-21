import utils


def filter_tokens(tokens: list[str], position: int, sign: int) -> list[str]:
    if len(tokens) == 1:
        return tokens
    zero_cnt = 0
    one_cnt = 0
    for i in range(len(tokens)):
        zero_cnt += 1 if tokens[i][position] == "0" else 0
        one_cnt += 1 if tokens[i][position] == "1" else 0
    if one_cnt >= zero_cnt:
        bit_criteria = "1" if sign > 0 else "0"
    else:
        bit_criteria = "0" if sign > 0 else "1"

    result = [x for x in tokens if x[position] == bit_criteria]
    if result:
        return result
    return [tokens[-1]]


def main():
    with utils.open_input_file(day=3) as stdin:
        tokens = []
        while True:
            current = next(utils.read_tokens(stdin, str), None)
            if not current:
                break
            tokens.append(current)

        oxygen = [*tokens]
        co2 = [*tokens]

        for i in range(len(tokens[0])):
            oxygen = filter_tokens(oxygen, i, 1)
            co2 = filter_tokens(co2, i, -1)

        print(int(oxygen[0], 2) * int(co2[0], 2))


main()
