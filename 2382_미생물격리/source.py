import sys


def solution(n, m, k, cells):
    # 상1 하2 좌3 우4
    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]
    for t in range(m):
        stack = {}
        for cell_idx in range(len(cells)):
            x, y, num, dir = cells[cell_idx]
            nx = x + dx[dir]
            ny = y + dy[dir]
            ndir = dir
            if nx == 0 or nx == n - 1:
                num //= 2
                ndir = 3 - dir
            if ny == 0 or ny == n - 1:
                num //= 2
                ndir = 7 - dir

            # check if cells overlapped
            if (nx, ny) in stack:
                stack[(nx, ny)][0].append(num)
                stack[(nx, ny)][1].append(ndir)
            else:
                stack[(nx, ny)] = [[num], [ndir]]

        # merge overlapped cells
        for k, v in stack.items():
            if len(v[0]) == 1:
                continue
            idx = v[0].index(max(v[0]))
            stack[k] = [[sum(v[0])], [v[1][idx]]]

        # rearrange cells
        cells = []
        for k, v in stack.items():
            cells.append([k[0], k[1], v[0][0], v[1][0]])

    answer = sum([x[2] for x in cells])

    return answer


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n, m, k = map(int, input().split())
        cells = [list(map(int, input().split())) for _ in range(k)]
        print("#%d %d" % (i, solution(n, m, k, cells)))
