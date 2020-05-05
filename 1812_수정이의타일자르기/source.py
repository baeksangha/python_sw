import sys


def solution(n, m, nums):
    nums.sort()
    answer = 1
    paper = m*m
    for num in nums:
        side = 1 << num
        if paper >= side*side:
            paper -= side**2
        else:
            paper = m*m
            answer += 1
    return answer


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n, m = map(int, input().split())
        nums = list(map(int, input().split()))
        print("#%d %d" % (i, solution(n, m, nums)))
