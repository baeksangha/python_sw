import sys
import math


def solution(n, nums):
    board = [[math.inf for _ in range(n)] for _ in range(n)]
    board[0][0] = nums[0][0]
    for i in range(1, n):
        board[0][i] = board[0][i-1] + nums[0][i]
        board[i][0] = board[i-1][0] + nums[i][0]
    for i in range(1, n):
        for j in range(1, n):
            board[i][j] = min(board[i-1][j], board[i][j-1]) + nums[i][j]
    return board[-1][-1]


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n = int(input())
        nums = [list(map(int, input().split())) for _ in range(n)]
        print("#%d %d" % (i, solution(n, nums)))
