import sys


def solution(n, m, times):
    times.sort()
    l = 0
    r = times[0] * m * 2
    answer = r // 2
    while l <= r:
        mid = (l + r) // 2
        sum_ = sum(mid // x for x in times)
        if sum_ < m:
            l = mid + 1
        else:
            r = mid - 1
            answer = min(answer, mid)
    return answer


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n, m = map(int, input().split())
        times = [int(input()) for _ in range(n)]
        print("#%d %d" % (i, solution(n, m, times)))
