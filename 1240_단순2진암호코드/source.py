import sys


def solution(n, m, arr):
    code = []
    decipher = {"0001101": 0, "0011001": 1, "0010011": 2, "0111101": 3, "0100011": 4, "0110001": 5,
                "0101111": 6, "0111011": 7, "0110111": 8, "0001011": 9}
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if arr[i][j] == '1':
                code = arr[i][j-55:j+1]
                break

    code_str = ["".join(code[7*x:7*x+7]) for x in range(8)]
    ver = 0
    ret = 0
    for i in range(len(code_str)):
        if code_str[i] not in decipher:
            return 0
        token = decipher[code_str[i]]
        ret += token
        if i % 2 == 0:
            ver += 3 * token
        else:
            ver += token

    if ver % 10 == 0:
        return ret
    else:
        return 0


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n, m = map(int, input().split())
        arr = [list(input()) for _ in range(n)]
        print("#%d %d" % (i, solution(n, m, arr)))
