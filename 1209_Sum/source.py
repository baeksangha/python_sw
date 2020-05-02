import sys


def solution(board):
    answer = 0
    for i in range(100):
        garo = board[i]
        sero = [board[x][i] for x in range(100)]
        answer = max(answer, sum(garo), sum(sero))
    diag1 = [board[x][x] for x in range(100)]
    diag2 = [board[x][99-x] for x in range(100)]
    answer = max(answer, sum(diag1), sum(diag2))
    return answer


if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    # tests = int(input())
    tests = 10
    for i in range(1, tests+1):
        n = int(input())
        board = [list(map(int, input().split())) for _ in range(100)]
        print("#%d %d" % (i, solution(board)))
