import utils


def main():
    result = 0
    with utils.open_input_file(day=8) as stdin:
        while True:
            digits = [*utils.read_tokens(stdin, str, r"[| \n]+")]
            if len(digits) == 0:
                break
            for digit in digits[-4:]:
                if len(digit) in [2, 3, 4, 7]:
                    result += 1

    print(result)


main()
