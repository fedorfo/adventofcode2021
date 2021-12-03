from typing import Optional

import utils


def main():
    with open(f"inputs/day3.in", "r") as stdin:
        tokens = []
        while stdin.readable():
            current = next(utils.read_tokens(stdin, str), None)
            if not current:
                break
            tokens.append(current)

        gamma = ""
        epsilon = ""

        for i in range(len(tokens[0])):
            zero_cnt = 0
            one_cnt = 0
            for j in range(len(tokens)):
                zero_cnt += 1 if tokens[j][i] == "0" else 0
                one_cnt += 1 if tokens[j][i] == "1" else 0
            if one_cnt >= zero_cnt:
                epsilon += "1"
                gamma += "0"
            else:
                gamma += "1"
                epsilon += "0"

        print(f"{int(gamma, 2)*int(epsilon, 2)}\n")


main()
