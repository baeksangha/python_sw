import sys


def is_run(arr):
    arr = list(set(arr))
    arr.sort()
    if len(arr) < 3:
        return 0
    cnt = 1
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1] + 1:
            cnt += 1
            if cnt == 3:
                return 1
        else:
            cnt = 1
    return 0


def is_triple(arr):
    d = {}
    for n in arr:
        if n in d:
            d[n] += 1
            if d[n] == 3:
                return 1
        else:
            d[n] = 1
    return 0


def solution(nums):
    a, b = [], []
    for i in range(len(nums)):
        if i % 2 == 0:
            a += [nums[i]]
            if is_triple(a) or is_run(a):
                return 1
        else:
            b += [nums[i]]
            if is_triple(b) or is_run(b):
                return 2
    return 0


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        nums = list(map(int, input().split()))
        print("#%d %d" % (i, solution(nums)))
