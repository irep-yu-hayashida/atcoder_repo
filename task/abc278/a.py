"""abc278_a"""
from sys import stdin


def main():
    N, K = map(int, stdin.readline().split())
    a_line = stdin.readline().split()
    del a_line[:K]
    for _ in range(K):
        a_line.append("0")
    return " ".join(a_line[:N])


if __name__ == "__main__":
    res = main()
    print(res)
