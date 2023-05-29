"""abc270
https://atcoder.jp/contests/abc081/tasks/abc081_b
"""
from sys import stdin
from typing import List, Union


def main():
    N: str

    N = int(input())
    A: List[int] = list(map(int, input().split()))

    count: int = 0
    flag = True
    while flag:
        n = sum(list(map(division_bool, A)))
        A = list(map(division, A))
        if n == N:
            count += 1
        else:
            flag = False

    print(count)


def division_bool(x: int) -> bool:
    return x % 2 == 0


def division(x: int) -> Union[int, float]:
    return x / 2


if __name__ == "__main__":
    main()
