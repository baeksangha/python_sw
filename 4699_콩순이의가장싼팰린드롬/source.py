import sys
import math

min_cost = []


def solution(l, string, costs):

    prices = [min(x) for x in costs]
    if len(string) == 0 or len(string) == 1:
        return 0
    min_cost[0] = [0 for _ in range(l+1)]
    min_cost[1] = [0 for _ in range(l+1)]
    # i: 팰린드롬의 길이, j: 시작 index
    for i in range(2, l+1):
        for j in range(l-i+1):
            substr = string[j:j+i]
            min_cost[i][j] = min(min_cost[i][j], min_cost[i-1][j] + prices[ord(substr[-1])-ord('a')])
            min_cost[i][j] = min(min_cost[i][j], min_cost[i-1][j+1] + prices[ord(substr[0])-ord('a')])
            if substr[0] == substr[-1]:
                min_cost[i][j] = min(min_cost[i][j], min_cost[i-2][j+1])

    return min_cost[-1][0]


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        l, k = map(int, input().split())
        string = input()
        min_cost = [[math.inf for _ in range(l+1)] for _ in range(l+1)]
        costs = [list(map(int, input().split())) for _ in range(k)]
        print("#%d %d" % (i, solution(l, string, costs)))
