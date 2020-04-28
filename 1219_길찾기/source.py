import sys


def solution(r1, r2):
    queue = [0]
    while queue:
        cur = queue.pop(0)
        if cur == 99:
            return 1
        if r1.get(cur):
            queue.append(r1[cur])
        if r2.get(cur):
            queue.append(r2[cur])
    return 0


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    # tests = int(input())
    tests = 10
    for i in range(1, tests+1):
        n, l = map(int, input().split())
        routes = list(map(int, input().split()))
        r1 = {}
        r2 = {}
        for j in range(0, l*2, 2):
            if r1.get(routes[j]):
                r2[routes[j]] = routes[j+1]
            else:
                r1[routes[j]] = routes[j+1]
        print("#%d %d" % (i, solution(r1, r2)))
