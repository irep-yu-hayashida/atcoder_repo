"""abc270"""
from sys import stdin


def main():
    N, Q = map(int, stdin.readline().split())
    user_status = dict()
    for _ in range(Q):
        T, A, B = map(int, stdin.readline().split())
        if T == 1:
            if user_status.get(A):
                user_status[A][B] = True
            else:
                user_status[A] = {B: True}
        elif T == 2:
            if user_status.get(A):
                user_status[A][B] = False
        elif T == 3:
            if user_status.get(A, {}).get(B, False) and user_status.get(B, {}).get(
                A, False
            ):
                print("Yes")
            else:
                print("No")


if __name__ == "__main__":
    main()
