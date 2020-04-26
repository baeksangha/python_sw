import sys


def convert(num):
    if num % 2 == 0:
        return num // 2
    else:
        return (num // 2) + 1


def solution(move):
    answer = 0
    n = len(move)
    moved = [0] * n
    aisle = []
    for elem in move:
        aisle.append([convert(elem[0]), convert(elem[1])])
    aisle = sorted([sorted(x) for x in aisle])
    print(aisle)
    for i in range(n):
        if moved[i] == 1:
            continue
        moved[i] = 1
        cur = [aisle[i]]
        for j in range(i+1, n):
            overlap = 0
            if moved[j] == 1:
                continue
            for student in cur:
                if student[1] >= aisle[j][0]:
                    overlap = 1
                    break
            if overlap == 0:
                moved[j] = 1
                cur.append(aisle[j])
        answer += 1
    return answer


if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n = int(input())
        move = []
        for _ in range(n):
            move.append(list(map(int, input().split())))
        print("#%d %d" % (i, solution(move)))
