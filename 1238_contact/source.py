import sys


def solution(board, start):
    queue = []
    edges = {}
    n = len(board)
    visited = [0 for _ in range(n)]

    visited[start] = 1
    for i in range(n):
        if board[start][i] == 1:
            queue.append((i, 1))
            edges[i] = 1
    while queue:
        vertex, value = queue[0]
        queue = queue[1:]
        visited[vertex] = 1
        for i in range(n):
            if board[vertex][i] == 0:
                continue
            if not edges.get(i):
                edges[i] = value + 1
                queue.append((i, value+1))

    edges = sorted(edges.items(), key=lambda x: (-x[1], -x[0]))
    return edges[0][0]


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    # tests = int(input())
    tests = 10
    for i in range(1, tests+1):
        datas, start = map(int, input().split())
        nums = list(map(int, input().split()))
        board = [[0 for _ in range(max(nums)+1)] for _ in range(max(nums)+1)]
        for j in range(0, len(nums), 2):
            board[nums[j]][nums[j+1]] = 1
        print("#%d %d" % (i, solution(board, start)))
