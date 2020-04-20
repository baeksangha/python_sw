import sys


def solution(manager):
    print(manager)
    return 0


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        manager = input()
        print("#%d %d" % (i, solution(manager)))
