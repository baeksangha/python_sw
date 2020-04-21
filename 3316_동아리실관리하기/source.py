import sys


def solution(manager):
    bitmask = [[0 for _ in range(16)] for _ in range(len(manager))]
    num = 1000000007
    for i in range(16):
        if i & 1 << 0 and i & (1 << (ord(manager[0]) - 65)):
            bitmask[0][i] = 1

    for i in range(1, len(manager)):
        flag = 1 << (ord(manager[i]) - 65)
        for j in range(16):
            if flag & j:
                for k in range(16):
                    if j & k:
                        bitmask[i][j] = (bitmask[i][j] + bitmask[i-1][k]) % num

    answer = 0
    for i in range(16):
        answer = (answer + bitmask[-1][i]) % num
    return answer


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        manager = input()
        print("#%d %d" % (i, solution(manager)))
