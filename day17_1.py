import utils


def main():
    with utils.open_input_file(day=17, example=False) as stdin:
        [xd, xu, yd, yu] = [*utils.read_tokens(stdin, int, r"[a-z:\. =,\n]")]
    best_vx, best_vy, best_maxy = 0, 0, 0
    for vx in range(0, 400):
        for vy in range(-400, 400):
            cmaxy = 0
            cvx, cvy = vx, vy
            cx, cy = 0, 0
            while True:
                if cx > xu or cy < yd:
                    break
                if cx in range(xd, xu + 1) and cy in range(yd, yu + 1):
                    if best_maxy < cmaxy:
                        best_maxy = cmaxy
                    break
                cx += cvx
                cy += cvy
                cmaxy = max(cmaxy, cy)
                cvx = cvx - 1 if cvx > 0 else 0
                cvy = cvy - 1

    print(f"{best_maxy}")


main()
