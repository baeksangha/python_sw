import sys


def solution(n, m):
    if n // 10 == 0:
        return n
    datas = [n]
    for i in range(m):
        new_datas = set()
        for data in datas:
            nlist = list(str(data))
            for j in range(len(nlist)):
                for k in range(j + 1, len(nlist)):
                    nlist[j], nlist[k] = nlist[k], nlist[j]
                    new_datas.add(int("".join(nlist)))
                    nlist = list(str(data))
        datas = new_datas
        # print(datas)

    return max(datas)


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n, m = map(int, input().split())
        print("#%d %d" % (i, solution(n, m)))
