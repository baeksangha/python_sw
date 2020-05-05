import sys


def solution(n, times):
    answer = 0
    times = sorted(times, key=lambda x: (x[1]-x[0], x[0]))
    work = []
    for time in times:
        s, e = time
        is_possible = 1
        for w in work:
            if w[0] < e and w[1] > s:
                is_possible = 0
                break
        if is_possible:
            answer += 1
            work.append((s, e))
    return answer


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n = int(input())
        times = [list(map(int, input().split())) for _ in range(n)]
        print("#%d %d" % (i, solution(n, times)))
