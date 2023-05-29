"""abc277_a
https://atcoder.jp/contests/abc083/tasks/abc083_b
"""
from sys import stdin


def get_sum(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n /= 10


def main():
    N, A, B = map(int, input().split())
    cnt = 0
    for i in range(N):
        sum = get_sum(i)
        if sum >= A and sum <= B:
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
