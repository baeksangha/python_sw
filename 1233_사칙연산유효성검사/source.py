import sys
import math


def solution(tree, cur, end, flag):
    # tree[cur]이 연산자일 때
    if flag == 0:
        if cur * 2 + 1 > end:
            return 0
        left = tree[cur*2]
        right = tree[cur*2+1]
        if '0' <= left <= '9':
            r1 = solution(tree, 2*cur, end, 1)
        else:
            r1 = solution(tree, 2*cur, end, 0)

        if '0' <= right <= '9':
            r2 = solution(tree, 2*cur+1, end, 1)
        else:
            r2 = solution(tree, 2*cur+1, end, 0)

        if r1 and r2:
            return 1
        return 0
    # tree[cur]이 숫자일 때
    if flag == 1:
        if cur * 2 > end:
            return 1
        else:
            return 0


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    # tests = int(input())
    tests = 10
    for i in range(1, tests+1):
        n = int(input())
        tree = [-1] * (int(pow(2, math.ceil(math.log2(n)))) + 1)
        for j in range(n):
            line = input().split()
            idx = int(line[0])
            token = line[1]
            tree[idx] = token
        if '0' <= tree[1] <= '9':
            ret = solution(tree, 1, n, 1)
        else:
            ret = solution(tree, 1, n, 0)
        print("#%d %d" % (i, ret))
