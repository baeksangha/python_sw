from itertools import combinations
import sys
import math


def solution(n, points):

    xs = [x[0] for x in points]
    ys = [x[1] for x in points]
    combs = list(map(list, combinations([x for x in range(n)], n//2)))

    answer = math.inf
    for comb in combs:
        x_sum = sum([xs[x] if x in comb else -xs[x] for x in range(n)])
        y_sum = sum([ys[x] if x in comb else -ys[x] for x in range(n)])
        answer = min(answer, x_sum**2+y_sum**2)
    return answer


if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n = int(input())
        points = [list(map(int, input().split())) for _ in range(n)]
        print("#%d %d" % (i, solution(n, points)))
