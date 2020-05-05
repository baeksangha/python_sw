import sys


def solution(n, m, weights, tons):
    answer = 0
    weights.sort(reverse=True)
    tons.sort(reverse=True)
    w_idx, t_idx = 0, 0
    while w_idx < len(weights) and t_idx < len(tons):
        if weights[w_idx] <= tons[t_idx]:
            t_idx += 1
            answer += weights[w_idx]
        w_idx += 1
    return answer


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n, m = map(int, input().split())
        weights = list(map(int, input().split()))
        tons = list(map(int, input().split()))
        print("#%d %d" % (i, solution(n, m, weights, tons)))
