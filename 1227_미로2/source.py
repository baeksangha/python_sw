import sys


def solution(board):
    queue = []
    visited = [[0 for _ in range(100)] for _ in range(100)]

    for i in range(100):
        for j in range(100):
            if board[i][j] == 2:
                queue = [(i, j)]
                break

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while queue:
        x, y = queue.pop(0)
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 100 and 0 <= ny < 100:
                if board[nx][ny] == 3:
                    return 1
                if board[nx][ny] == 0 and visited[nx][ny] == 0:
                    queue.append((nx, ny))

    return 0


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    # tests = int(input())
    tests = 10
    for i in range(1, tests+1):
        n = int(input())
        board = [list(map(int, list(input()))) for _ in range(100)]
        print("#%d %d" % (i, solution(board)))
