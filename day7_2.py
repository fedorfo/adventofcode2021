import utils


def main():
    with utils.open_input_file(day=7) as stdin:
        crab_positions = [*utils.read_tokens(stdin, int, r"[, \n]+")]

    distance = [0]
    for i in range(1, max(crab_positions) - min(crab_positions) + 1):
        distance.append(distance[-1] + i)

    best_result = 10 ** 18
    for i in range(min(crab_positions), max(crab_positions) + 1):
        result = 0
        for position in crab_positions:
            result += distance[abs(position - i)]
        if result < best_result:
            best_result = result
    print(best_result)


main()
