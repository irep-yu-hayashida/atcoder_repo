"""abc278_d"""
# データの持ち方に注意。デフォルト値を設定しておけるデータ形式の方有利。データアクセスの速度問題？
from sys import stdin
from typing import Tuple


def main():
    sequence = Sequence(int(stdin.readline()), list(map(int, stdin.readline().split())))
    Q = int(stdin.readline())

    for _ in range(Q):
        query: Tuple[int, int | None, int | None] = tuple(
            map(int, stdin.readline().split())
        )
        if query[0] == 1:
            sequence.request1(query[1])
        elif query[0] == 2:
            sequence.request2(query[1], query[2])
        elif query[0] == 3:
            sequence.request3(query[1])


class Sequence:
    def __init__(self, N, sequence):
        self.N = N
        self.origin = [0] * N
        self.diff = self.origin.copy()
        self.base = None
        self.sequence = sequence

    def request1(self, base: int):
        self.base = base
        self.diff = self.origin.copy()

    def request2(self, idx, increment):
        self.diff[idx - 1] += increment

    def request3(self, idx):
        if self.base == None:
            print(self.diff[idx - 1] + self.sequence[idx - 1])

        else:
            print((self.diff[idx - 1] + self.base))


if __name__ == "__main__":
    main()
