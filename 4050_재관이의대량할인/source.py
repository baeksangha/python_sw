import sys


def solution(prices):
    answer = 0
    prices.sort(reverse=True)
    for i in range(len(prices)):
        if i % 3 != 2:
            answer += prices[i]
    return answer


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n = int(input())
        prices = list(map(int, input().split()))
        print("#%d %d" % (i, solution(prices)))
