import sys


def solution(n, m, board):
    answer = 0
    for phase in range(1, 22):
        loss = phase ** 2 + (phase - 1) ** 2
        for x in range(n):
            for y in range(n):
                house = 0
                for i in range(phase):
                    st_x = x - phase + 1 + i
                    st_y = y - i
                    for j in range(2*i+1):
                        if 0 <= st_x < n and 0 <= st_y+j < n and board[st_x][st_y+j] == 1:
                            house += 1
                for i in range(phase-1):
                    st_x = x + 1 + i
                    st_y = y - phase + 2 + i
                    for j in range(2*phase-3-2*i):
                        if 0 <= st_x < n and 0 <= st_y+j < n and board[st_x][st_y+j] == 1:
                            house += 1
                profit = house * m
                if profit - loss >= 0:
                    answer = max(answer, house)
    return answer


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n, m = map(int, input().split())
        board = [list(map(int, input().split())) for _ in range(n)]
        print("#%d %d" % (i, solution(n, m, board)))
