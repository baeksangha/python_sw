import sys


def get_max(worker, c):
    n = 2**len(worker)
    ret = 0
    for i in range(n):
        honey_sum = 0
        profit = 0
        for j in range(len(worker)):
            if i & (1 << j):
                honey_sum += worker[j]
                profit += worker[j]**2
        if honey_sum <= c:
            ret = max(ret, profit)
    return ret


def solution(n, m, c, board):
    board_1d = [y for x in board for y in x]
    answer = 0
    len_1d = n**2 - m + 1
    for i in range(len_1d):
        if i // n != (i + m - 1) // n:
            continue
        worker1 = board_1d[i:i+m]
        for j in range(i+m, n**2):
            if j // n != (j + m - 1) // n:
                worker2 = board_1d[j:((j//n)+1)*n]
            else:
                worker2 = board_1d[j:j+m]
            part_max = get_max(worker1, c) + get_max(worker2, c)
            answer = max(answer, part_max)

    return answer


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n, m, c = map(int, input().split())
        board = [list(map(int, input().split())) for _ in range(n)]
        print("#%d %d" % (i, solution(n, m, c, board)))
