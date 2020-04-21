import sys

forward = [0] * 16


def solution(n, ranks, cache, state):

    if state == (1 << n) - 1:
        return 1
    if cache[state] != -1:
        return cache[state]

    cache[state] = 0
    for i in range(n):
        if (state & (1 << i)) or ((state & forward[i]) != forward[i]):
            continue
        cache[state] += solution(n, ranks, cache, (state | (1 << i)))

    return cache[state]


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n, m = map(int, input().split())
        ranks = [list(map(int, input().split())) for _ in range(m)]
        forward = [0] * n
        for r in ranks:
            forward[r[1]-1] |= 1 << (r[0]-1)
        print("#%d %d" % (i, solution(n, ranks, [-1 for _ in range(1 << n)], 0)))
