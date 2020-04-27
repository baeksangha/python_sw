import sys


def solution(x, y, z, a, b, c, n):
    x_line = [0] * n
    y_line = [0] * n
    z_line = [0] * n
    xy_line = [0] * n
    xyz_line = [0] * n

    for i in range(x):
        x_line[abs(i-a) % n] += 1
    for i in range(y):
        y_line[abs(i-b) % n] += 1
    for i in range(z):
        z_line[abs(i-c) % n] += 1

    for i in range(n):
        for j in range(n):
            xy_line[(i+j) % n] += x_line[i] * y_line[j]
    for i in range(n):
        for j in range(n):
            xyz_line[(i+j) % n] += xy_line[i] * z_line[j]
    return " ".join(list(map(str, xyz_line)))


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        x, y, z, a, b, c, n = map(int, input().split())
        print("#%d %s" % (i, solution(x, y, z, a, b, c, n)))
