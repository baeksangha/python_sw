import sys

m_cpu = 0
answer = 99999


def can_draw(cpu, board, d):
    x, y = cpu
    n = len(board)
    if d == 0:
        for i in range(y):
            if board[x][i] != 0:
                return False
    elif d == 1:
        for i in range(y+1, n):
            if board[x][i] != 0:
                return False
    elif d == 2:
        for i in range(x):
            if board[i][y] != 0:
                return False
    elif d == 3:
        for i in range(x+1, n):
            if board[i][y] != 0:
                return False
    return True


def draw_line(board, x, y, d, flag):
    ret = 0
    n = len(board)
    nums = [2, 0]
    if d == 0:
        for i in range(y):
            board[x][i] = nums[flag]
            ret += 1
    elif d == 1:
        for i in range(y+1, n):
            board[x][i] = nums[flag]
            ret += 1
    elif d == 2:
        for i in range(x):
            board[i][y] = nums[flag]
            ret += 1
    elif d == 3:
        for i in range(x+1, n):
            board[i][y] = nums[flag]
            ret += 1
    return ret


def recur(cpus, board, idx, max_cpus, length):
    global m_cpu
    global answer
    if idx == len(cpus):
        if m_cpu < max_cpus:
            answer = length
            m_cpu = max_cpus
        elif m_cpu == max_cpus:
            answer = min(answer, length)
    else:
        for i in range(4):
            if can_draw(cpus[idx], board, i):
                x, y = cpus[idx][0], cpus[idx][1]
                recur(cpus, board, idx+1, max_cpus+1, length + draw_line(board, x, y, i, 0))
                draw_line(board, x, y, i, 1)
        recur(cpus, board, idx+1, max_cpus, length)


def solution(n, board):
    processes = []
    for i in range(1, n-1):
        for j in range(1, n-1):
            if board[i][j] == 1:
                processes.append([i, j])
    recur(processes, board, 0, 0, 0)


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n = int(input())
        board = [list(map(int, input().split())) for _ in range(n)]
        answer = 99999
        m_cpu = 0
        solution(n, board)
        print("#%d %d" % (i, answer))
