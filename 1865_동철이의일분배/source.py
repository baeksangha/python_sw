import sys

percents = []
answer = 0


def norm(a):
    return int(a)/100


def dfs(n, p, idx, visited):
    global answer
    if p <= answer:
        return
    if idx == n:
        answer = max(answer, p)
        return
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            dfs(n, p * percents[idx][i], idx+1, visited)
            visited[i] = 0


def solution(n):
    global answer
    answer = 0
    visited = [0 for _ in range(n)]
    dfs(n, 100, 0, visited)
    return answer


if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n = int(input())
        percents = [list(map(norm, input().split())) for _ in range(n)]
        print("#%d %.6f" % (i, solution(n)))
