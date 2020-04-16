import sys


def solution(m, n):


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n, m = map(int, input().split())
        board = [[0 for _ in range(n+1)] for _ in range(n+1)]
        for _ in range(m):
            x, y = map(int, input().split())
            board[x][y] = 1
        print("#%d %d" % (i, solution(m, n)))
