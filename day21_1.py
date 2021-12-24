import numpy

import utils

dice_rolls = 0


def next_dice_value(dice_value: int) -> int:
    global dice_rolls
    dice_rolls += 1
    if dice_value < 100:
        return dice_value + 1
    else:
        return 1


def normalize_position(position: int) -> int:
    position = position % 10
    if position == 0:
        return 10
    return position


def main():
    with utils.open_input_file(day=21, example=False) as stdin:
        positions = [int(stdin.readline().split(": ")[1]) for _ in range(2)]
    scores = [0, 0]
    player = 0
    dice_value = 0
    while True:
        step = 0
        for _ in range(3):
            dice_value = next_dice_value(dice_value)
            step += dice_value
        positions[player] = normalize_position(positions[player] + step)
        scores[player] += positions[player]
        if scores[player] >= 1000:
            break
        player = 1 - player
    print(f"{scores[1-player]*dice_rolls}")


main()
