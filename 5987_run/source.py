import sys


def solve(flag):
    print("before", dp, flag)
    if flag == full:
        return 1

    if dp[flag] != -1:
        return dp[flag]
    dp[flag] = 0

    for i in range(n):
        if (flag & 1 << i) == 0 and (flag & needs[i]) == needs[i]:
            dp[flag] += solve(flag | 1 << i)
    print("after", dp, flag)
    return dp[flag]


sys.stdin = open('input', 'r')
for T in range(1, int(input()) + 1):

    n, m = map(int, input().split())
    needs = [0] * 16
    dp = [-1] * (1 << n)

    for i in range(m):
        a, b = map(int, input().split())
        needs[b - 1] |= 1 << (a - 1)
    full = (1 << n) - 1
    print('#%d %d' % (T, solve(0)))
    print(needs)
    print(dp)
