'''
삼원일차방정식의 해를 구하는 방법을 고민했는데
a, b, c 셋다 1부터 20까지의 수라 모든 경우를 고려해보아도 되었다.
'''

import sys


def get_candidates(done):
    a = b = c = 0
    res = []
    for line in done:
        dots = 0
        for char in line:
            if char == '.':
                dots += 1
            else:
                break
        if a or b or c:
            res += [(a, b, c, dots)]
        a += line.count("(") - line.count(")")
        b += line.count("{") - line.count("}")
        c += line.count("[") - line.count("]")

    res = list(set(res))

    ret = []
    all_clear = len(res)
    for i in range(1, 21):
        for j in range(1, 21):
            for k in range(1, 21):
                cnt = 0
                for elem in res:
                    a, b, c, value = elem
                    if a * i + b * j + c * k == value:
                        cnt += 1
                    else:
                        break
                if cnt == all_clear:
                    ret += [(i, j, k)]

    return ret


def solution(done, todo):
    answer = []
    candidates = get_candidates(done)

    rr = cc = ss = 0

    for line in todo:
        if not (rr or cc or ss):
            answer.append(0)
        else:
            token = set()
            for candidate in candidates:
                r, c, s = candidate
                token.add(r*rr + c*cc + s*ss)
            if len(token) == 1:
                answer.append(list(token)[0])
            else:
                answer.append(-1)
        rr += line.count("(") - line.count(")")
        cc += line.count("{") - line.count("}")
        ss += line.count("[") - line.count("]")

    return list(map(str, answer))


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        p, q = map(int, input().split())
        done = [input() for _ in range(p)]
        todo = [input() for _ in range(q)]
        print("#%d %s" % (i, ' '.join(solution(done, todo))))
