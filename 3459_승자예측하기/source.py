import sys
import math


down_up = [3]
up_down = [2]


def get_arr():
    for i in range(60):
        if i % 2 == 0:
            down_up.append(down_up[-1]*2)
            up_down.append(up_down[-1]*2 + 1)
        else:
            down_up.append(down_up[-1]*2 + 1)
            up_down.append(up_down[-1]*2)


def solution(n):
    index = int(math.log2(n))
    order = n - int(pow(2, index))
    if n == 1:
        return "Bob"
    if index % 2 == 0:
        if order < int(pow(2, index-1)):
            return "Alice"
        else:
            a_max = down_up[index-1]-1
            if (int(pow(2, index)) + int(pow(2, index-1))) <= n <= a_max:
                return "Alice"
            else:
                return "Bob"
    else:
        if order > int(pow(2, index-1)):
            return "Alice"
        else:
            b_max = up_down[index-1]-1
            if int(pow(2, index)) <= n <= b_max:
                return "Bob"
            else:
                return "Alice"


if __name__ == "__main__":
    get_arr()
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n = int(input())
        print("#%d %s" % (i, solution(n)))
