import sys


def find(a, root):
    while a != root[a]:
        a = root[a]
    return a


def union(a, b, rank, root):
    a, b = max(a, b), min(a, b)
    root_a = find(a)
    root_b = find(b)
    if rank[root_a] > rank[root_b]:
        root[root_b] = a
    else:
        root[root_a] = b
        if rank[root_a] == rank[root_b]:
            rank[root_b] += 1


def solution(v, edges):
    root = [i for i in range(v)]
    rank = [0 for _ in range(v)]
    answer = 0
    edges = sorted(edges, key=lambda x: (x[2], x))
    idx = 0

    while idx < len(edges):
        a, b, value = edges[idx]
        a, b = a - 1, b - 1
        root_a, root_b = find(a, root), find(b, root)
        if root_a != root_b:
            answer += value
            union(a, b)
        idx += 1

    print(edges)
    return answer


if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        v, e = map(int, input().split())
        edges = [list(map(int, input().split())) for _ in range(e)]
        print("#%d %d" % (i, solution(v, edges)))
