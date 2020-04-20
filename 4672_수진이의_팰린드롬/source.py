import sys


def solution(string):
    answer = 0
    dict_ = {}
    for s in string:
        if s in dict_:
            dict_[s] += 1
        else:
            dict_[s] = 1

    for _, v in dict_.items():
        answer += v * (v + 1) // 2

    return answer


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        inp = input()
        print("#%d %d" % (i, solution(inp)))
