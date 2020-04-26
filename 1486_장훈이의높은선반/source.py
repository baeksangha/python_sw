import sys
from itertools import combinations


def solution(n, b, talls):
    answer = 200000
    for i in range(1, n+1):
        comb_list = list(map(list, (combinations(talls, i))))
        for elem in comb_list:
            p_sum = sum(elem)
            if p_sum >= b:
                answer = min(answer, p_sum)
    return answer - b


if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n, b = map(int, input().split())
        talls = list(map(int, input().split()))
        print("#%d %d" % (i, solution(n, b, talls)))
