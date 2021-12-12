import utils


def main():
    with utils.open_input_file(day=6) as stdin:
        numbers = [*utils.read_tokens(stdin, int, r"[, \n]+")]
    lanternfish_count = [0 for _ in range(9)]
    for number in numbers:
        lanternfish_count[number] += 1

    for _ in range(80):
        lanternfish_count1 = [*lanternfish_count[1:], 0]
        lanternfish_count1[6] += lanternfish_count[0]
        lanternfish_count1[8] = lanternfish_count[0]
        lanternfish_count = lanternfish_count1

    print(sum(lanternfish_count))


main()
