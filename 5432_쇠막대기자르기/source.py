import sys


def solution(pipe):
    answer = 0
    n_pipes = 0
    paren_cnt = 0
    for i in range(0, len(pipe)-1):
        if pipe[i] == "(" and pipe[i+1] == ")":
            answer += paren_cnt
        elif pipe[i] == "(":
            n_pipes += 1
            paren_cnt += 1
        elif pipe[i] == ")" and pipe[i-1] == "(":
            continue
        else:
            paren_cnt -= 1
    return answer + n_pipes


if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        pipe = input()
        print("#%d %d" % (i, solution(pipe)))
