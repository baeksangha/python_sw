import sys


def solution(string):
    arr = string.split("&&")
    equals = {}
    unequals = {}
    filt = []
    for line in arr:
        if '==' in line:
            l, r = line.split('==')
        else:
            continue


    for line in filt:
        if '==' in line:
            l, r = sorted(line.split('=='), key=lambda x: x.isalpha())
            if not l.isalpha():
                if l not in equals or (l in equals and len(equals[l]) > len(r)):
                    equals[l] = r
        else:
            l, r = sorted(line.split('!='), key=lambda x: -x.isalpha())
            unequals[l] = r
    print("==:", equals)
    print("!=:", unequals)
    print(arr)
    return ""


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    testcases = int(input())
    for i in range(testcases):
        string = input()
        print("%s" % solution(string))
