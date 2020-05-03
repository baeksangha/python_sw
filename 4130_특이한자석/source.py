import sys


def rotate(magnet, flag):
    # clockwise
    if flag == 1:
        return [magnet[-1]] + magnet[:-1]
    # counter clockwise
    else:
        return magnet[1:] + [magnet[0]]


def solution(k, magnets, commands):
    answer = 0
    for cmd in commands:
        target, flag = cmd[0]-1, cmd[1]
        l_idx = r_idx = target
        l_flag = flag * -1
        while l_idx > 0 and magnets[l_idx][6] != magnets[l_idx-1][2]:
            l_idx -= 1
        while r_idx < 3 and magnets[r_idx][2] != magnets[r_idx+1][6]:
            r_idx += 1
        for i in range(target-1, l_idx-1, -1):
            magnets[i] = rotate(magnets[i], l_flag)
            l_flag *= -1
        for i in range(target, r_idx+1):
            magnets[i] = rotate(magnets[i], flag)
            flag *= -1

    for i in range(4):
        if magnets[i][0] == 1:
            answer += (1 << i)
    return answer


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        k = int(input())
        magnets = [list(map(int, input().split())) for _ in range(4)]
        commands = [list(map(int, input().split())) for _ in range(k)]
        print("#%d %d" % (i, solution(k, magnets, commands)))
