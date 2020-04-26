import sys


def solution(points):
    possible = set([0])
    points.sort()
    idx = 0
    while idx < len(points):
        tmp = tuple(possible)
        for elem in tmp:
            possible.add(elem + points[idx])
        possible.add(points[idx])
        idx += 1

    return len(possible)


if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n = int(input())
        points = list(map(int, input().split()))
        print("#%d %d" % (i, solution(points)))
