from typing import TextIO, Optional

import utils


class Board:
    __slots__ = ("_content", "_marked", "_last_marked")

    def __init__(self, content: list[list[int]]) -> None:
        assert len(content) == 5
        for line in content:
            assert len(line) == 5
            for number in line:
                assert isinstance(number, int)
        self._content = content
        self._marked = [[False] * 5 for _ in range(5)]
        self._last_marked = 0

    @staticmethod
    def scan(input_stream: TextIO) -> Optional["Board"]:
        line = input_stream.readline()
        if line != "\n":
            return None
        content = [[*utils.read_tokens(input_stream, int, " ")] for _ in range(5)]
        return Board(content)

    def mark(self, number: int):
        for i in range(5):
            for j in range(5):
                if self._content[i][j] == number:
                    self._marked[i][j] = True
        self._last_marked = number

    def _is_all_marked(self, *, i0: int, j0: int, iv: int, jv: int):
        while True:
            if i0 not in range(5) or j0 not in range(5):
                return True
            if not self._marked[i0][j0]:
                return False
            i0 += iv
            j0 += jv

    def is_bingo(self) -> bool:
        results = []
        for x in range(5):
            results.append(self._is_all_marked(i0=0, j0=x, iv=1, jv=0))
            results.append(self._is_all_marked(i0=x, j0=0, iv=0, jv=1))
        return any(results)

    def get_score(self) -> int:
        sum = 0
        for i in range(5):
            for j in range(5):
                if not self._marked[i][j]:
                    sum += self._content[i][j]
        return sum * self._last_marked


def main():
    with utils.open_input_file(day=4) as stdin:
        numbers = [*utils.read_tokens(stdin, int, ",")]
        boards: list[Board] = []
        while True:
            board = Board.scan(stdin)
            if not board:
                break
            boards.append(board)

        for number in numbers:
            for board in boards:
                board.mark(number)
                if board.is_bingo():
                    print(board.get_score())
                    return


main()
