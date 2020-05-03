import sys


def solution(n, boxes):
    for i in range(n):
        s = set(boxes)
        if len(s) == 1 or (len(s) == 2 and max(s)-min(s) == 1):
            break
        boxes[boxes.index(max(boxes))] -= 1
        boxes[boxes.index(min(boxes))] += 1
    return max(boxes) - min(boxes)


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    # tests = int(input())
    tests = 10
    for i in range(1, tests+1):
        n = int(input())
        boxes = list(map(int, input().split()))
        print("#%d %d" % (i, solution(n, boxes)))
