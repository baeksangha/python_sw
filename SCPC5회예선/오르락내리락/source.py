import sys

arr = [0 for _ in range(1000001)]
sum_arr = [0 for _ in range(1000001)]


def initialize():
    arr[1], arr[2], arr[3], arr[4] = 0, 1, 3, 2
    sum_arr[1], sum_arr[2], sum_arr[3], sum_arr[4] = 0, 1, 4, 6
    for i in range(6, 1000001, 2):
        arr[i] = arr[i // 2] + 1
        arr[i - 1] = arr[i] + 1
        sum_arr[i - 1] = sum_arr[i - 2] + arr[i - 1]
        sum_arr[i] = sum_arr[i - 1] + arr[i]


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    test_cases = int(input())
    initialize()
    for i in range(1, test_cases+1):
        a, b = map(int, input().split())
        print("Case #%d\n%d" % (i, sum_arr[b]-sum_arr[a-1]))
