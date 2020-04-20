import sys


def solution(stopover):
    cur_x, cur_y = stopover[0]
    answer = 0
    for point in stopover:
        st_x, st_y = point
        if st_y > cur_y and st_x > cur_x:
            diag = min(st_x - cur_x, st_y - cur_y)
            answer += diag + (st_x - cur_x - diag) + (st_y - cur_y - diag)
        elif st_y < cur_y and st_x < cur_x:
            diag = min(cur_x - st_x, cur_y - st_y)
            answer += diag + (cur_x - st_x - diag) + (cur_y - st_y - diag)
        else:
            answer += abs(st_x - cur_x) + abs(st_y - cur_y)
        cur_x, cur_y = st_x, st_y
    return answer


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        w, h, n = map(int, input().split())
        xy = []
        for _ in range(n):
            xy.append(list(map(int, input().split())))
        print("#%d %d" % (i, solution(xy)))
