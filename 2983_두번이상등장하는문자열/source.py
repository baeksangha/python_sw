import sys


def solution(s, nums):
    answer = 0
    for num in nums:
        a, b = num
    return answer


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n, a = map(int, input().split())
        nums = [list(map(int, input().split())) for _ in range(n)]
        print("#%d %d" % (i, solution([a], nums)))
