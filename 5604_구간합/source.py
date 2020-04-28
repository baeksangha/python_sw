import sys
import math

arr = [0] * 10


def calc(n, flag):
    while n > 0:
        arr[n % 10] += (10 ** flag)
        n //= 10


def solution(a, b):
    index = 0
    while a != b:
        if a % 10 != 0:
            calc(a, index)
            a += 1
        elif b % 10 != 9:
            calc(b, index)
            b -= 1
        else:
            token = ((b // 10 - a // 10) + 1) * (10 ** index)
            a //= 10
            b //= 10
            for i in range(10):
                arr[i] += token
            index += 1
    if a == b:
        calc(a, index)
    sum_ = sum([i*arr[i] for i in range(10)])
    return sum_


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        arr = [0] * 10
        a, b = map(int, (input().split()))
        print("#%d %d" % (i, solution(a, b)))
