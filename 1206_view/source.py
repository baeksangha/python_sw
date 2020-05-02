import sys


def solution(n, complex):
    answer = 0
    for i in range(2, n-2):
        max_lr = max(complex[i-2], complex[i-1], complex[i+1], complex[i+2])
        if complex[i] - max_lr > 0:
            answer += complex[i] - max_lr
    return answer


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    # tests = int(input())
    tests = 10
    for i in range(1, tests+1):
        n = int(input())
        complex = list(map(int, input().split()))
        print("#%d %d" % (i, solution(n, complex)))
