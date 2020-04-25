import sys
import math


def solution(n, rooms):
    answer = math.inf
    nears = [[1 for _ in range(n)] for _ in range(n)]
    di = [0, 0, -1, 1]
    dj = [-1, 1, 0, 0]
    max_value = 1
    for i in range(n):
        for j in range(n):
            if nears[i][j] != 1:
                continue
            queue = [(i, j)]
            while queue:
                x, y = queue.pop()
                for k in range(4):
                    nx = x + di[k]
                    ny = y + dj[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if rooms[nx][ny] == rooms[x][y] + 1:
                            nears[nx][ny] = nears[x][y]+1
                            max_value = max(max_value, nears[nx][ny])
                            queue.append((nx, ny))
    for i in range(n):
        for j in range(n):
            if nears[i][j] == max_value:
                answer = min(answer, rooms[i][j])
    return [str(answer - max_value + 1), str(max_value)]


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n = int(input())
        rooms = [list(map(int, input().split())) for _ in range(n)]
        print("#%d %s" % (i, " ".join(solution(n, rooms))))
