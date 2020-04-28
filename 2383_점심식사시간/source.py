import math
import sys


def down(stair, people, time):
    if not people:
        return 0

    dist = []
    x, y = stair
    for person in people:
        dist.append(abs(person[0]-x) + abs(person[1]-y))
    dist.sort()

    if len(dist) <= 3:
        return dist[-1] + time

    times = [dist[0]+time, dist[1]+time, dist[2]+time]
    for i in range(3, len(dist)):
        if times[i-3] > dist[i]:
            next_time = times[i-3] + time - 1
        else:
            next_time = dist[i] + time
        times.append(next_time)
    return max(times)


def solution(n, board):
    stairs = []
    people = []
    answer = math.inf
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                continue
            elif board[i][j] == 1:
                people.append((i, j))
            else:
                stairs.append((i, j))
    cases = 2 ** len(people)

    for i in range(cases):
        stair_1 = []
        stair_2 = []
        for j in range(len(people)):
            if i & (2 ** j):
                stair_1.append(people[j])
            else:
                stair_2.append(people[j])
        s1 = down(stairs[0], stair_1, board[stairs[0][0]][stairs[0][1]]+1)
        s2 = down(stairs[1], stair_2, board[stairs[1][0]][stairs[1][1]]+1)
        answer = min(answer, max(s1, s2))

    return answer


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n = int(input())
        board = [list(map(int, input().split())) for _ in range(n)]
        print("#%d %d" % (i, solution(n, board)))
