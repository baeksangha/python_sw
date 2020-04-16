import sys


def get_pow(m, n):
    num = 1000000007
    if n == 1:
        return m

    if n % 2 == 0:
        half = get_pow(m, n//2)
        return (half * half) % num
    else:
        return (get_pow(m, n-1) * m) % num


def solution(m, n):
    num = 1000000007
    comb_triangle = [[1 for _ in range(m+1)] for _ in range(m+1)]
    for i in range(2, m+1):
        for j in range(1, i):
            comb_triangle[i][j] = (comb_triangle[i-1][j] + comb_triangle[i-1][j-1]) % num

    fp = [0] * (m + 1)
    for i in range(1, m+1):
        fp[i] = get_pow(i, n)

    for i in range(2, m+1):
        for j in range(1, i):
            fp[i] = (fp[i] - (comb_triangle[i][j] * fp[j]) % num) % num
            if fp[i] < 0:
                fp[i] += num

    return fp[-1]


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        m, n = map(int, input().split())
        print("#%d %d" % (i, solution(m, n)))
