import sys


def solution(board):

    for i in range(9):
        garo = board[i]
        if len(set(garo)) != 9:
            return 0
        sero = [x[i] for x in board]
        if len(set(sero)) != 9:
            return 0
        rem, quo = i % 3, i // 3
        nemo = []
        for y in range(quo*3, quo*3+3):
            nemo += board[y][rem*3:rem*3+3]
        if len(set(nemo)) != 9:
            return 0

    return 1


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        # n = int(input())
        board = [list(map(int, input().split())) for _ in range(9)]
        print("#%d %d" % (i, solution(board)))
