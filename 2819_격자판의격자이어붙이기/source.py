import sys

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]


def recur(board, x, y, idx, ret):
    if idx == 7:
        return [ret]

    result = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 4 and 0 <= ny < 4:
            result += recur(board, nx, ny, idx+1, ret+str(board[nx][ny]))

    return result


def solution(board):
    s = set()
    for i in range(4):
        for j in range(4):
            ret = tuple(recur(board, i, j, 1, str(board[i][j])))
            for e in ret:
                s.add(e)
    return len(s)


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        board = [list(map(int, input().split())) for _ in range(4)]
        print("#%d %d" % (i, solution(board)))
