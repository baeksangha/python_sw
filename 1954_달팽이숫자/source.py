import sys


def solution(n):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    dir = 0
    cnt = 1
    visited = [[0 for _ in range(n)] for _ in range(n)]
    answer = [[0 for _ in range(n)] for _ in range(n)]
    visited[0][0] = 1
    answer[0][0] = 1
    cx, cy = 0, 0
    num = 2
    while cnt < n**2:
        nx, ny = cx + dx[dir], cy + dy[dir]
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
            cx, cy = nx, ny
            visited[nx][ny] = 1
            answer[nx][ny] = num
            num += 1
            cnt += 1
        else:
            dir = (dir + 1) % 4

    for e in answer:
        print(" ".join(list(map(str, e))))


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n = int(input())
        print("#%d" % i)
        solution(n)
