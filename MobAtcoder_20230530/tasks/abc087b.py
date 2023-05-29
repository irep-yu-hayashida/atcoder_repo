"""abc271_c"""
from sys import stdin


def main():
	a, b, c = map(int, input().split())
    X = int(input())
    count = 0
    for i in range(a):
        for j in range(b):
            for k in range(c):
                if i*500 + j*100 + k*50 == X:
                    count += 1
    print(count)

if __name__ == "__main__":
    main()