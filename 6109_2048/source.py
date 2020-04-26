import sys


def solution(board, cmd):
    dic = {"left": 0, "down": 1, "right": 2, "up": 3}
    rt = dic[cmd]
    for _ in range(rt):
        board = [list(x) for x in zip(*board[::-1])]

    n = len(board)
    for i in range(n):
        idx = 1
        tmp = []
        for j in range(n):
            if board[i][j] != 0:
                tmp.append(board[i][j])
        while idx < len(tmp):
            if tmp[idx-1] == tmp[idx]:
                tmp[idx-1] *= 2
                del tmp[idx]
            idx += 1
        tmp += [0] * (n - len(tmp))
        board[i] = tmp

    while rt % 4 != 0:
        board = [list(x) for x in zip(*board[::-1])]
        rt += 1

    return board


if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n, cmd = input().split()
        n = int(n)
        board = []
        for j in range(n):
            board.append(list(map(int, input().split())))
        ret = solution(board, cmd)
        print("#%d" % i)
        for elem in ret:
            print(' '.join(str(x) for x in elem))
