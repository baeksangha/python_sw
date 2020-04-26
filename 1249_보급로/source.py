# 421 403
import sys
import math


def solution(n, board):
    min_cost = [[math.inf for _ in range(n)] for _ in range(n)]
    visited = [[0 for _ in range(n)] for _ in range(n)]
    min_cost[0][0] = 0
    queue = [(0, 0)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while queue:
        x, y = queue.pop()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if min_cost[nx][ny] > min_cost[x][y] + board[nx][ny]:
                    min_cost[nx][ny] = min_cost[x][y] + board[nx][ny]
                    queue.append((nx, ny))
                elif visited[nx][ny] == 0:
                    queue.append((nx, ny))
    return min_cost[n-1][n-1]


if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n = int(input())
        board = [list(map(int, input())) for _ in range(n)]
        print("#%d %.0f" % (i, solution(n, board)))
