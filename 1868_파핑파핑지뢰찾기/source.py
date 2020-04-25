import sys


def expand(i, j, board):
    queue = [[i, j]]
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    while queue:
        x, y = queue.pop()
        board[x][y] = 'x'
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(board) and 0 <= ny < len(board) and board[nx][ny] != '*':
                if board[nx][ny] == ".":
                    queue.append([nx, ny])
                else:
                    board[nx][ny] = 'x'


def solution(n, board):
    answer = 0

    # 지뢰 갯수 표시
    m_dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    m_dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    for x in range(n):
        for y in range(n):
            if board[x][y] == '*':
                for k in range(8):
                    nx = x + m_dx[k]
                    ny = y + m_dy[k]
                    if 0 <= nx < len(board) and 0 <= ny < len(board) and board[nx][ny] != "*":
                        if board[nx][ny] == ".":
                            board[nx][ny] = "1"
                        else:
                            board[nx][ny] = chr(ord(board[nx][ny]) + 1)
    # 0들 찾기
    for x in range(n):
        for y in range(n):
            if board[x][y] == '.':
                answer += 1
                expand(x, y, board)

    # 나머지들 정리
    for x in range(n):
        for y in range(n):
            if board[x][y] != '*' and board[x][y] != 'x':
                answer += 1

    return answer


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n = int(input())
        board = [list(input()) for _ in range(n)]
        print("#%d %d" % (i, solution(n, board)))
