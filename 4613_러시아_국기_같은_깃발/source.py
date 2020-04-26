import sys


def solution(board):
    answer = 2500
    n = len(board)
    m = len(board[0])

    w = []
    b = []
    r = []

    for i in range(n):
        w.append(m - board[i].count("W"))
        b.append(m - board[i].count("B"))
        r.append(m - board[i].count("R"))

    for i in range(1, n-1):
        for j in range(i+1, n):
            token = sum(w[:i]) + sum(b[i:j]) + sum(r[j:])
            answer = min(token, answer)
    return answer


if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n, m = map(int, input().split())
        board = []
        for _ in range(n):
            board.append(input())
        print("#%d %d" % (i, solution(board)))
