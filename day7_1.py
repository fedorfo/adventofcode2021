import utils


def main():
    with utils.open_input_file(day=7) as stdin:
        crab_positions = [*utils.read_tokens(stdin, int, r"[, \n]+")]

    best_result = 10 ** 18
    for i in range(min(crab_positions), max(crab_positions) + 1):
        result = 0
        for position in crab_positions:
            result += abs(position - i)
        if result < best_result:
            best_result = result
    print(best_result)


main()
