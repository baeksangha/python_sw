import math
import sys

primes = [2]

def get_primes():
    for i in range(3, 1000001):
        cnt = 0
        for p in primes:
            if p * p > i:
                break
            if i % p == 0:
                cnt = 1
                break
        if cnt == 0:
            primes.append(i)


def solution(d, left, right):
    answer = 0
    for p in primes:
        if p > right:
            break
        if left <= p <= right and str(d) in str(p):
            answer += 1
    return answer


if __name__ == "__main__":
    get_primes()
    sys.stdin = open('input','r')
    tests = int(input())
    for i in range(1, tests+1):
        d, a, b = map(int, input().split())
        print("#%d %d" % (i, solution(d, a, b)))
