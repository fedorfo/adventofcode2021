from collections import defaultdict

import utils


def do_iteration(pairs: dict[str, int], rules: dict[str, str]) -> dict[str, int]:
    result = defaultdict(lambda: 0)
    for k, v in pairs.items():
        first, second = k[0] + rules[k], rules[k] + k[1]
        result[first] = result[first] + v
        result[second] = result[second] + v
    return result


def main():
    with utils.open_input_file(day=14, example=False) as stdin:
        [formula] = [*utils.read_tokens(stdin, str)]
        utils.read_tokens(stdin)
        rules = {}
        while True:
            rule = [*utils.read_tokens(stdin, str, separator="[ \n>-]+")]
            if not rule:
                break
            rules[rule[0]] = rule[1]
    pairs = defaultdict(lambda: 0)
    for i in range(len(formula) - 1):
        pair = formula[i] + formula[i + 1]
        pairs[pair] = pairs[pair] + 1

    for _ in range(40):
        pairs = do_iteration(pairs, rules)

    count = defaultdict(lambda: 0)
    for k, v in pairs.items():
        for x in k:
            count[x] = count[x] + v
    count = {k: (v+1) // 2 for k, v in count.items()}
    result = max([v for k, v in count.items()]) - min([v for k, v in count.items()])
    print(result)


main()
