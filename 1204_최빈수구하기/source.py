import sys


def solution(n, arr):
    dic = {}
    for num in arr:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1

    sorted_dic = sorted(dic.items(), key=lambda x: (-x[1], -x[0]))
    return sorted_dic[0][0]


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n = int(input())
        arr = list(map(int, input().split()))
        print("#%d %d" % (i, solution(n, arr)))
