import sys


def solution(a, b):

    f1 = [1, 3, 6, 10, 15, 21, 100]
    f2 = [5000000, 3000000, 2000000, 500000, 300000, 100000, 0]
    s1 = [1, 3, 7, 15, 31, 64]
    s2 = [5120000, 2560000, 1280000, 640000, 320000, 0]

    p1 = 0
    if a > 0:
        idx1 = 0
        while f1[idx1] < a:
            idx1 += 1
        p1 = f2[idx1]
    p2 = 0
    if b > 0:
        idx2 = 0
        while s1[idx2] < b:
            idx2 += 1
        p2 = s2[idx2]
    return p1 + p2


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        a, b = map(int, input().split())
        print("%d" % solution(a, b))
