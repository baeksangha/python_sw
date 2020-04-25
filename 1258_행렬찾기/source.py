import sys

board = []


def solution(n):
    queue = []
    matrices = []
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0 and board[i][j] != -1:
                queue.append((i, j))
                garo, sero = j, i
                while queue:
                    x, y = queue.pop()
                    garo, sero = max(garo, y), max(sero, x)
                    board[x][y] = -1
                    if y + 1 < n and board[x][y+1] != 0 and board[x][y+1] != -1:
                        queue.append((x, y+1))
                    if x + 1 < n and board[x+1][y] != 0 and board[x+1][y] != -1:
                        queue.append((x+1, y))
                h = garo - j + 1
                v = sero - i + 1
                matrices.append([v, h])

    matrices = sorted(matrices, key=lambda x:(x[0]*x[1], x[0]))
    matrices = [str(y) for x in matrices for y in x]

    return len(matrices)//2, " ".join(matrices)


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n = int(input())
        board = [list(map(int, input().split())) for _ in range(n)]
        n_ret, list_ret = solution(n)
        print("#%d %d %s" % (i, n_ret, list_ret))
