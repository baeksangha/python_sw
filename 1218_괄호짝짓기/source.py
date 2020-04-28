import sys


def solution(parens):
    p_dict = {'(': 1, '[': 2, '<': 3, '{': 4, ')': -1, ']': -2, '>': -3, '}': -4}
    stack = []
    for c in parens:
        flag = p_dict[c]
        if flag > 0:
            stack.append(flag)
        else:
            if stack[-1] + flag == 0:
                stack.pop()
            else:
                return 0
    return 1


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    # tests = int(input())
    tests = 10
    for i in range(1, tests+1):
        l = int(input())
        string = input()
        print("#%d %d" % (i, solution(string)))
