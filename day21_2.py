import numpy

import utils


def normalize_position(position: int) -> int:
    position = position % 10
    if position == 0:
        return 10
    return position


def main():
    with utils.open_input_file(day=21, example=False) as stdin:
        positions = [int(stdin.readline().split(": ")[1]) for _ in range(2)]
    dp = numpy.array([0] * 31 * 31 * 11 * 11 * 2).reshape([31, 31, 11, 11, 2])
    dp[0][0][positions[0]][positions[1]][0] = 1

    for score1 in range(21):
        for score2 in range(21):
            for position1 in range(1, 11):
                for position2 in range(1, 11):
                    for player in range(2):
                        for step1 in range(1, 4):
                            for step2 in range(1, 4):
                                for step3 in range(1, 4):
                                    step = step1 + step2 + step3
                                    if player == 0:
                                        position_n1 = normalize_position(position1 + step)
                                        score_n1 = score1 + position_n1
                                        position_n2 = position2
                                        score_n2 = score2
                                    else:
                                        position_n1 = position1
                                        score_n1 = score1
                                        position_n2 = normalize_position(position2 + step)
                                        score_n2 = score2 + position_n2

                                    value = dp[score1][score2][position1][position2][player]
                                    if value > 0:
                                        dp[score_n1][score_n2][position_n1][position_n2][1 - player] += value

    win_sum = [0, 0]
    for score in range(21, 31):
        for opponent_score in range(21):
            for position in range(1, 11):
                for opponent_position in range(1, 11):
                    win_sum[0] += dp[score][opponent_score][position][opponent_position][1]
                    win_sum[1] += dp[opponent_score][score][position][opponent_position][0]

    print(f"{max(win_sum[0], win_sum[1])}")


main()
