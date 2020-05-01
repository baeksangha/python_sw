import sys

decipher = [[2, 1, 1], [2, 2, 1], [1, 2, 2], [4, 1, 1], [1, 3, 2],
            [2, 3, 1], [1, 1, 4], [3, 1, 2], [2, 1, 3], [1, 1, 2]]


def decode(code, degree):
    cur = '0'
    ratio = []
    ret = ''
    # print(degree, code)
    for i in range(len(code)):
        if code[i] != cur and len(ratio) != 3:
            cur = code[i]
            ratio.append(1)
        elif code[i] == cur and ratio:
            ratio[-1] += 1
        if (code[i] != cur and len(ratio) == 3) or i == len(code) - 1:
            cur = code[i]
            coprime = [ratio[x] // degree for x in range(3)]
            for i in range(10):
                if coprime == decipher[i]:
                    ret += str(i)
            ratio = []
    # print(ret)
    return ret


def get_degree(line, idx):
    reverse = 0
    cur = '1'
    idx -= 1
    ratio = [1]
    while idx >= 0:
        if line[idx] != cur:
            cur = line[idx]
            reverse += 1
            if reverse == 3:
                break
            ratio = [1] + ratio
        else:
            ratio[0] += 1
        idx -= 1
    for i in range(10):
        s = set([ratio[x] / decipher[i][x] for x in range(3)])
        if len(s) == 1:
            return int(list(s).pop())
    return -1


def solution(n, m, arr):

    codes = set()
    for i in range(n):
        new_line = []
        for j in range(m):
            new_line += list(bin(int(arr[i][j], 16))[2:].zfill(4))
        idx = len(new_line) - 1
        while idx >= 0:
            if new_line[idx] != '0':
                degree = get_degree(new_line, idx)
                codes.add(("".join(new_line[idx-degree*56+1:idx+1]), degree))
                idx -= degree*56
            else:
                idx -= 1

    ret = 0
    for elem in codes:
        code, degree = elem
        new_code = decode(code, degree)
        check = 0
        for i in range(len(new_code)):
            if i % 2 == 0:
                check += int(new_code[i]) * 3
            else:
                check += int(new_code[i])
        if check % 10 == 0:
            ret += sum([int(x) for x in new_code])

    return ret


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n, m = map(int, input().split())
        arr = [list(input()) for _ in range(n)]
        print("#%d %d" % (i, solution(n, m, arr)))
