import sys

arr = [0 for _ in range(1000001)]


def get_prime():

    for i in range(1, 1000001, 2):
        for j in range(1, 1000001):
            if i * j <= 1000000:
                arr[i*j] += i
            else:
                break

    for i in range(1, 1000001):
        arr[i] += arr[i-1]


def solution(l, r):
    answer = arr[r] - arr[l-1]
    return answer


if __name__ == "__main__":
    get_prime()
    # print(arr[:100])
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        l, r = map(int, input().split())
        print("#%d %d" % (i, solution(l, r)))
