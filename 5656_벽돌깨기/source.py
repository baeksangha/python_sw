import sys
import math


def rotate(board, num):
    ret = [x[:] for x in board]
    for i in range(num):
        ret = [list(x) for x in zip(*reversed(ret))]
    return ret


def swipe(board, x, y):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    scale = board[x][y]
    queue = [(x, y, scale)]
    ret = [x[:] for x in board]
    h, w = len(board), len(board[0])
    # swipe bricks
    while queue:
        x, y, scale = queue.pop(0)
        ret[x][y] = 0
        for i in range(4):
            for s in range(1, scale):
                nx, ny = x + dx[i]*s, y + dy[i]*s
                if 0 <= nx < h and 0 <= ny < w and ret[nx][ny] != 0:
                    queue.append((nx, ny, ret[nx][ny]))

    # arrange
    ret = rotate(ret, 1)
    for i in range(len(ret)):
        tmp = []
        for j in range(len(ret[i])):
            if ret[i][j] != 0:
                tmp.append(ret[i][j])
        ret[i] = tmp + [0]*(len(ret[i])-len(tmp))
    ret = rotate(ret, 3)
    return ret


def brickout(n, num, board):
    if n == num:
        res = sum([len(x)-x.count(0) for x in board])
        return res

    h, w = len(board), len(board[0])
    ret = math.inf
    for i in range(w):
        for j in range(h):
            if board[j][i] != 0:
                new_board = swipe(board, j, i)
                ret = min(ret, brickout(n, num+1, new_board))
                break

    return ret


def solution(n, board):
    answer = brickout(n, 0, board)
    if answer == math.inf:
        return 0
    else:
        return answer


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n, w, h = map(int, input().split())
        board = [list(map(int, input().split())) for _ in range(h)]
        print("#%d %d" % (i, solution(n, board)))
