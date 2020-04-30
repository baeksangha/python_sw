import sys


def solution(n, m, k, board):
    s = set()
    alive = []
    breeding = []

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(n):
        for j in range(m):
            if board[i][j] != 0:
                alive.append((i, j, 0, board[i][j]))
                s.add((i, j))

    for cur_time in range(1, k+1):
        # breeding
        compete = {}
        for i in range(len(breeding)):
            x, y, k = breeding[i]
            for j in range(4):
                tx = x + dx[j]
                ty = y + dy[j]
                if (tx, ty) in s:
                    continue
                if compete.get((tx, ty)):
                    compete[(tx, ty)].append((tx, ty, cur_time, k))
                else:
                    compete[(tx, ty)] = [(tx, ty, cur_time, k)]

        for k, v in compete.items():
            vv = sorted(v, key=lambda x: x[3], reverse=True)
            alive.append(vv[0])
            s.add((vv[0][0], vv[0][1]))

        breeding = []

        # add breeding
        alive.sort(key=lambda x: x[2]+2*x[3])
        for i in range(len(alive)):
            x, y, t, k = alive[i]
            if cur_time == t + k:
                breeding.append((x, y, k))

        # rearrange alive
        idx = 0
        for i in range(len(alive)):
            x, y, t, k = alive[i]
            if t + 2*k > cur_time:
                idx = i
                break
        alive = alive[idx:]

    return len(alive)


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n, m, k = map(int, input().split())
        board = [list(map(int, input().split())) for _ in range(n)]
        print("#%d %d" % (i, solution(n, m, k, board)))
