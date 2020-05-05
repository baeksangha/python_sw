import sys
from decimal import Decimal


def solution(n, k, pers):
    answer = Decimal('Infinity')
    pers = [Decimal(str(x)) for x in pers]
    acc_sum = [sum(pers[:x]) for x in range(1, n+1)]
    acc_sq_sum = [sum([pers[y]*pers[y] for y in range(x)]) for x in range(1, n+1)]
    for i in range(n):
        for j in range(k, n+1):
            if i+j > n:
                break
            start = i - 1
            end = i + j - 1
            if start < 0:
                sq_avg = acc_sq_sum[end] / j
                avg_sq = (acc_sum[end] / j) ** 2
            else:
                sq_avg = (acc_sq_sum[end] - acc_sq_sum[start]) / j
                avg_sq = ((acc_sum[end] - acc_sum[start]) / j) ** 2
            v = sq_avg - avg_sq
            answer = min(v, answer)
    return answer.sqrt()


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    n, k = map(int, input().split())
    pers = list(map(int, input().split()))
    print("%.14lf" % solution(n, k, pers))
