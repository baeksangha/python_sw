import sys


def get_line_beans(line):
    if line % 4 == 1 or line % 4 == 2:
        return (line // 2) + 1
    else:
        return (line + 1) // 2


def solution(n, m):
    garo = get_line_beans(n)
    sero_o = get_line_beans(m)
    if m % 4 == 1 or m % 4 == 2:
        sero_x = (m - 1) // 2
    else:
        sero_x = m // 2

    answer = (sero_o * garo) + (sero_x * (n - garo))

    return answer


if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n, m = map(int, input().split())
        print("#%d %d" % (i, solution(n, m)))
