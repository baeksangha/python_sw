import sys


def solution(board):
    n = 100
    answer = []
    for i in range(n):
        if board[0][i] == 0:
            continue
        x, y = 1, i
        length = 1
        while x < n:
            if y > 0 and board[x][y-1] == 1:
                while y > 0 and board[x][y-1] == 1:
                    y -= 1
                    length += 1
            elif y < n-1 and board[x][y+1] == 1:
                while y < n-1 and board[x][y+1] == 1:
                    y += 1
                    length += 1
            x += 1
            length += 1
        answer.append((length, i))
    answer = sorted(answer, key=lambda x: (x[0], -x[1]))

    return answer[0][1]


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    # tests = int(input())
    tests = 10
    for i in range(1, tests+1):
        n = int(input())
        board = [list(map(int, input().split())) for _ in range(100)]
        print("#%d %d" % (i, solution(board)))
