import sys


def solution(p, q):
    if p % q == 0:
        return str(p // q)
    digit = [str(p // q), '.']
    numerator = {}
    token = (p % q) * 10
    idx = 2
    while not numerator.get(token):
        numerator[token] = idx
        digit += [str(token // q)]
        token = token % q * 10
        idx += 1
    idx = numerator[token]

    block = "".join(digit[idx:])
    if block == "0":
        return p / q
    else:
        return "".join(digit[:idx]) + "(" + block + ")"


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        p, q = map(int, input().split())
        print("#%d %s" % (i, solution(p, q)))
