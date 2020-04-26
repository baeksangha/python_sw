import sys


def solution(cams, k):
    cams = sorted(set(cams))
    dist = []
    for i in range(1, len(cams)):
        dist.append(cams[i] - cams[i-1])
    if k >= len(cams):
        return 0
    for _ in range(k-1):
        dist.remove(max(dist))
    return sum(dist)


if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n = int(input())
        k = int(input())
        cams = list(map(int, input().split()))
        print("#%d %d" % (i, solution(cams, k)))
