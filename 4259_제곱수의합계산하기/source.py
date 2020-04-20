import sys


def solution(nums):
    answer = 0

    for num in nums:
        answer += int(pow(num // 10, num % 10))

    return answer


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n = int(input())
        nums = list(map(int, input().split()))
        print("#%d %d" % (i, solution(nums)))
