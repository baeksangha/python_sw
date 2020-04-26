import sys


def get_nums(a):
    ret = 0
    sta = str(a)
    n = len(sta)
    digit = n - 1
    idx = 0
    while idx < n:
        if int(sta[idx]) >= 4:
            ret += (int(sta[idx]) - 1) * int(pow(9, digit))
        else:
            ret += int(sta[idx]) * int(pow(9, digit))
        digit -= 1
        idx += 1

    return ret


def solution(a, b):
    answer = 0
    if a * b > 0:
        if a < 0:
            a = -a
            b = -b
        answer += abs(get_nums(b) - get_nums(a))
    else:
        a = -a
        answer += get_nums(a) + get_nums(b) - 1

    return answer


if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n, m = map(int, input().split())
        print("#%d %d" % (i, solution(n, m)))
