import sys


def solution(x, y, z, a, b, c, n):
    answer = 0

    return answer


if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        x, y, z, a, b, c, n = map(int, input().split())
        print("#%d %d" % (i, solution(x, y, z, a, b, c, n)))
