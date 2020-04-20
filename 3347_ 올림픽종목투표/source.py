import sys


def solution(event, com):
    votes = {}
    for c in com:
        for i in range(len(event)):
            if c >= event[i]:
                if votes.get(i+1):
                    votes[i+1] += 1
                else:
                    votes[i+1] = 1
                break
    return sorted(votes.items(), key=lambda x:x[1], reverse=True)[0][0]


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n, m = map(int, input().split())
        ai = list(map(int, input().split()))
        bi = list(map(int, input().split()))
        print("#%d %d" % (i, solution(ai, bi)))
