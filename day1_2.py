import utils


def main():
    with utils.open_input_file(day=1) as stdin:
        previous_list: list[int] = []
        increments = 0
        while stdin.readable():
            current = next(utils.read_tokens(stdin, int), None)
            if current is None:
                break
            if len(previous_list) == 3:
                current_list = [*previous_list[1:], current]
                if sum(current_list) > sum(previous_list):
                    increments += 1
                previous_list = current_list
            else:
                previous_list.append(current)
        print(increments)


main()
