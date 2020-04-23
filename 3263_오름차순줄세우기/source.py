import sys


def solution(n, childs):
    print(childs)
    d = [0] * (n + 1)
    for i in range(n):
        d[childs[i]] = d[childs[i]-1] + 1
        print(d)

    return n - max(d)


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n = int(input())
        childs = list(map(int, input().split()))
        print("#%d %d" % (i, solution(n, childs)))
