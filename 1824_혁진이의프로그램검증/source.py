import sys


def solution(r, c, dp, board):

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    # x, y, direction, memory_value
    queue = [(0, 0, 1, 0)]

    while queue:
        x, y, d, value = queue.pop()
        dp[x][y][d][value] = 1
        flag = board[x][y]
        if "0" <= flag <= "9":
            value = int(flag)
        elif flag == '<' or (flag == '_' and value != 0):
            d = 0
        elif flag == '>' or (flag == '_' and value == 0):
            d = 1
        elif flag == '^' or (flag == '|' and value != 0):
            d = 2
        elif flag == 'v' or (flag == '|' and value == 0):
            d = 3
        elif flag == '+':
            value = (value + 1) % 16
        elif flag == '-':
            value = (value - 1) % 16
        elif flag == '@':
            return "YES"

        if flag == '?':
            for i in range(4):
                nx = (x + dx[i]) % r
                ny = (y + dy[i]) % c
                if not dp[nx][ny][i][value]:
                    queue.append((nx, ny, i, value))
        else:
            nx = (x + dx[d]) % r
            ny = (y + dy[d]) % c
            if not dp[nx][ny][d][value]:
                queue.append((nx, ny, d, value))
    return "NO"


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        r, c = map(int, input().split())
        dp = [[[[0 for _ in range(16)] for _ in range(4)] for _ in range(c)] for _ in range(r)]
        board = [list(input()) for _ in range(r)]
        print("#%d %s" % (i, solution(r, c, dp, board)))
