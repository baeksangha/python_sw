import sys


def check(line, idx, slope, flag):
    token = line[idx]
    # 0: 왼쪽, 1: 오른쪽
    if flag == 0:
        for i in range(slope):
            index = idx-1-i
            if index < 0 or line[index] != token - 1:
                return 0
        return 1
    else:
        for i in range(slope):
            index = idx+1+i
            if index >= len(line) or line[index] != token - 1:
                return 0
        return 1


def solution(n, slope, board):

    answer = 0
    lines = board + [[x[i] for x in board] for i in range(n)]
    built = set()

    for i in range(len(lines)):
        line = lines[i]
        # 높이 차가 2 이상 날 때
        if max([abs(line[i] - line[i+1]) for i in range(n-1)]) > 1:
            continue
        # 모든 높이가 똑같을 때
        if len(set(line)) == 1:
            answer += 1
            continue

        failed = 0
        for j in range(1, n):
            if line[j] == line[j-1] + 1:
                is_passed = check(line, j, slope, 0)
                if not is_passed:
                    failed = 1
                    break
                else:
                    for k in range(slope):
                        built.add((i, j-1-k))
        if failed:
            continue
        for j in range(n-1):
            if line[j] == line[j+1] + 1:
                is_passed = check(line, j, slope, 1)
                if not is_passed:
                    failed = 1
                    break
                else:
                    for k in range(slope):
                        if (i, j+1+k) in built:
                            failed = 1
                            break
                        built.add((i, j+1+k))
        if not failed:
            answer += 1

    return answer


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n, x = map(int, input().split())
        board = [list(map(int, input().split())) for _ in range(n)]
        print("#%d %d" % (i, solution(n, x, board)))
