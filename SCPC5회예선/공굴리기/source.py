import sys
import math


def solution(ball, hurdles):
    r, start, end = ball
    garo, sero, circle = end-start, 0, 0
    for hurdle in hurdles:
        h = hurdle[2]
        if h >= r:
            garo -= 2 * r
            sero += 2 * (h - r)
            circle += math.pi * r
        else:
            theta = math.acos((r-h)/r)
            garo -= 2 * r * math.sin(theta)
            circle += 2 * r * theta
    return garo + sero + circle


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    test_cases = int(input())
    for i in range(1, test_cases+1):
        ball = list(map(int, input().split()))
        n = int(input())
        hurdles = [list(map(int, input().split())) for _ in range(n)]
        print("Case #%d\n%.8f" % (i, solution(ball, hurdles)))
