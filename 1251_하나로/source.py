import sys
import math


def solution(n, x_points, y_points, e):
    edges = [[0 for _ in range(n)] for _ in range(n)]
    visited = [0 for _ in range(n)]
    arr = [math.inf for _ in range(n)]
    arr[0] = 0
    for i in range(n):
        for j in range(n):
            p1 = [x_points[i], y_points[i]]
            p2 = [x_points[j], y_points[j]]
            edges[i][j] = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

    while 0 in visited:
        min_value = math.inf
        cur = -1
        for i in range(n):
            if visited[i] == 0 and min_value > arr[i]:
                cur = i
                min_value = arr[i]
        visited[cur] = 1

        for i in range(n):
            if visited[i] == 0:
                arr[i] = min(arr[i], edges[cur][i])

    return sum(arr)*e


if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n = int(input())
        x_points = list(map(int, input().split()))
        y_points = list(map(int, input().split()))
        e = float(input())
        print("#%d %.0f" % (i, solution(n, x_points, y_points, e)))
