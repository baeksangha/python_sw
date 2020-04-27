import sys
import math

childs = {}


def solution(tree, cur):
    if tree[cur].isdigit():
        return int(tree[cur])
    else:
        if tree[cur] == "+":
            return solution(tree, childs[cur][0]) + solution(tree, childs[cur][1])
        elif tree[cur] == "-":
            return solution(tree, childs[cur][0]) - solution(tree, childs[cur][1])
        elif tree[cur] == "*":
            return solution(tree, childs[cur][0]) * solution(tree, childs[cur][1])
        else:
            return solution(tree, childs[cur][0]) // solution(tree, childs[cur][1])


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
            if len(line) > 2:
                childs[int(line[0])] = [int(line[2]), int(line[3])]
        ret = solution(tree, 1)
        print("#%d %d" % (i, ret))
