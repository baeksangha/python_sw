import sys


def solution(l, r, hurdles):
    print("l, r:", l, r)
    answer = 0
    hurdles.sort()
    for i in range(len(hurdles)):
        if hurdles[i][1] < 0:
            hurdles[i][1] *= -1

    for i in range(len(hurdles)-1):
        x, y = hurdles[i]
        if x < l:
            answer = max(min(l, hurdles[i+1][0])-x, answer)
        elif x > r:
            answer = max(x - max(r, hurdles[i-1][0]), answer)
        else:
            answer = max(answer, min(y, hurdles[i+1][0]-x))
    return answer*2


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    test_cases = int(input())
    for i in range(1, test_cases+1):
        l, r = map(int, input().split())
        n = int(input())
        hurdles = [list(map(int, input().split())) for _ in range(n)]
        print("Case #%d\n%d" % (i, solution(l, r, hurdles)))
