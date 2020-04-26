import sys


def solution(a, b):
    idx = 0
    answer = 0
    while idx < len(a):
        if a[idx:idx+len(b)] == b:
            idx += len(b)
        else:
            idx += 1
        answer += 1

    return answer


if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        a, b = input().split()
        print("#%d %d" % (i, solution(a, b)))
