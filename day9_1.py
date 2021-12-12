import utils


def main():
    with utils.open_input_file(day=9) as stdin:
        lines = []
        while True:
            line = stdin.readline().strip("\n")
            if not line:
                break
            lines.append(line)
        field = [
            [9] * (len(lines[0]) + 2),
            *[[9, *[ord(x) - ord("0") for x in line], 9] for line in lines],
            [9] * (len(lines[0]) + 2),
        ]

    result = 0
    for i in range(1, len(field)-1):
        for j in range(1, len(field[0]) - 1):
            if field[i][j] < min(field[i][j+1], field[i+1][j], field[i][j-1], field[i-1][j]):
                result += field[i][j]+1

    print(result)

main()
