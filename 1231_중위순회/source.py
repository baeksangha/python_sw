import sys
import math

childs = {}


def solution(tree, cur, n):
    if 2 * cur > n:
        return tree[cur]

    if 2 * cur + 1 > n:
        return solution(tree, 2*cur, n) + tree[cur]
    else:
        return solution(tree, 2*cur, n) + tree[cur] + solution(tree, 2*cur+1, n)


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    # tests = int(input())
    tests = 10
    for i in range(1, tests+1):
        n = int(input())
        tree = [-1] * (int(pow(2, math.ceil(math.log2(n)))) + 1)
        childs = {}
        for j in range(n):
            line = input().split()
            tree[int(line[0])] = line[1]
        ret = solution(tree, 1, n)
        print("#%d %s" % (i, ret))
