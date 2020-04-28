import sys


def solution(n, arr):
    flag = -1
    answer = 1
    for i in range(1, n):
        if flag == -1:
            if arr[i] > arr[i-1]:
                flag = 0
            elif arr[i] < arr[i-1]:
                flag = 1
        else:
            if flag == 0 and arr[i] < arr[i-1]:
                flag = -1
                answer += 1
            elif flag == 1 and arr[i] > arr[i-1]:
                flag = -1
                answer += 1
    return answer


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n = int(input())
        arr = list(map(int, (input().split())))
        print("#%d %d" % (i, solution(n, arr)))
