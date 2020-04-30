import sys


def norm(a):
    return int(a)-1


def solution(n, m, go):
    answer = 2500
    board = [[-1 for _ in range(n)] for _ in range(n)]
    half = n // 2

    board[half-1][half-1] = board[half][half] = 1
    board[half][half-1] = board[half-1][half] = 0

    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    for cmd in go:
        x, y, flag = cmd
        board[x][y] = flag
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            cnt = 0
            while 0 <= nx < n and 0 <= ny < n and board[nx][ny] != flag and board[nx][ny] != -1:
                cnt += 1
                nx, ny = nx + dx[i], ny + dy[i]
            if not (0 <= nx < n and 0 <= ny < n and board[nx][ny] == flag):
                continue
            nx, ny = x, y
            for j in range(cnt):
                nx, ny = nx + dx[i], ny + dy[i]
                board[nx][ny] = flag

    w, b = 0, 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                b += 1
            elif board[i][j] == 1:
                w += 1

    return " ".join([str(b), str(w)])


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n, m = map(int, input().split())
        go = []
        for _ in range(m):
            go.append(list(map(norm, input().split())))
        print("#%d %s" % (i, solution(n, m, go)))
