import sys

fact = [0, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
expo = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
weights = []
sum_weights = 0


def recur(left, right, visited, cnt):
    global sum_weights
    if left < right:
        return 0
    if cnt == len(visited):
        return 1

    if left >= sum_weights - left:
        return expo[len(visited)-cnt] * fact[len(visited)-cnt]

    ret = 0
    for i in range(len(visited)):
        if visited[i] == 0:
            visited[i] = 1
            if left >= right + weights[i]:
                ret += recur(left, right + weights[i], visited, cnt+1)
            ret += recur(left + weights[i], right, visited, cnt+1)
            visited[i] = 0
    return ret


def solution(n):
    answer = 0
    visited = [0 for _ in range(n)]
    for i in range(n):
        visited[i] = 1
        answer += recur(weights[i], 0, visited, 1)
        visited[i] = 0
    return answer


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n = int(input())
        weights = list(map(int, input().split()))
        sum_weights = sum(weights)
        print("#%d %s" % (i, solution(n)))
