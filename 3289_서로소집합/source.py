import sys


def find(parent, a):
    while parent[a] != a:
        a = parent[a]
    return parent[a]


def solution(n, sets):
    answer = ""
    parent = [x for x in range(n+1)]
    rank = [0 for _ in range(n+1)]
    for s in sets:
        flag, a, b = s
        a, b = max(a, b), min(a, b)
        root_a, root_b = find(parent, a), find(parent, b)
        if flag == 0:
            if rank[root_a] > rank[root_b]:
                parent[root_b] = root_a
            else:
                parent[root_a] = root_b
                if rank[root_a] == rank[root_b]:
                    rank[root_b] += 1
        else:
            if root_a == root_b:
                answer += "1"
            else:
                answer += "0"
        print("parent :", parent)
        print("rank :", rank)
    return answer


if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n, m = map(int, input().split())
        sets = [list(map(int, input().split())) for _ in range(m)]
        print("#%d %s" % (i, solution(n, sets)))
