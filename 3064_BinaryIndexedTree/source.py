import sys
import math

segtree = []
nodes = []


def init(node, start, end):
    if node >= len(segtree):
        return 0
    if start == end:
        segtree[node] = nodes[start]
        return segtree[node]
    else:
        left = init(node*2, start, (start+end)//2)
        right = init(node*2+1, ((start+end)//2)+1, end)
        segtree[node] = left + right
        return segtree[node]


def update(node, start, end, idx, value):
    if node >= len(segtree):
        return 0
    if idx < start or idx > end:
        return

    segtree[node] += value
    update(node*2, start, (start+end)//2, idx, value)
    update(node*2+1, ((start+end)//2)+1, end, idx, value)


def subsum(node, start, end, s_start, s_end):
    if s_start > end or s_end < start:
        return 0
    if s_start <= start and s_end >= end:
        return segtree[node]
    left = subsum(node*2, start, (start+end)//2, s_start, s_end)
    right = subsum(node*2+1, ((start+end)//2)+1, end, s_start, s_end)
    return left+right


def solution(n, commands):
    answer = []
    for command in commands:
        flag, a, b = command
        if flag == 1:
            update(1, 0, n-1, a-1, b)
        else:
            res = subsum(1, 0, n-1, a-1, b-1)
            answer.append(str(res))
    return " ".join(answer)


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n, m = map(int, input().split())
        nodes = list(map(int, input().split()))
        commands = [list(map(int, input().split())) for _ in range(m)]
        n_segtree = 1 << (math.ceil(math.log2(n)) + 1)
        segtree = [0] * n_segtree
        init(1, 0, n-1)
        print("#%d %s" % (i, solution(n, commands)))
