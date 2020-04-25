import sys
import math


def solution(nums, n):
    answer = 0
    aliquots = []
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            aliquots.append((n, n//i))


    return answer


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        nums = list(map(int, input().split()))
        n = int(input())
        print("#%d %d" % (i, solution(nums, n)))
