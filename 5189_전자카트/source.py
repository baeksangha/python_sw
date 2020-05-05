import math
import sys

edges = []


def solution(n, visited, cur, sum_):
    if 0 not in visited:
        return sum_ + edges[cur][0]

    ret = math.inf
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            ret = min(ret, solution(n, visited, i, sum_ + edges[cur][i]))
            visited[i] = 0
    return ret


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n = int(input())
        edges = [list(map(int, input().split())) for _ in range(n)]
        visited = [0 for _ in range(n)]
        visited[0] = 1
        print("#%d %d" % (i, solution(n, visited, 0, 0)))
