import sys
import math


def solution(r_time1, r_time2, arr_times, a, b):

    answer_a = set()
    answer_b = set()

    wait_1 = []
    wait_2 = []

    # [a, b] : 고객, 남은 시간
    desk_1 = {}
    desk_2 = {}

    arr_times.sort()
    # print(arr_times)
    cur = arr_times[0]
    idx = 0
    while idx < len(arr_times) or wait_1 or wait_2 or desk_1 or desk_2:

        # release finished seats
        remove_1 = []
        remove_2 = []
        for d in sorted(desk_1.keys()):
            if desk_1[d][1] == cur:
                wait_2.append((cur, d, desk_1[d][0]))
                remove_1.append(d)
        for d in sorted(desk_2.keys()):
            if desk_2[d][1] == cur:
                remove_2.append(d)
        for re in remove_1:
            desk_1.pop(re)
        for re in remove_2:
            desk_2.pop(re)

        wait_2.sort()
        # fill empty seats
        for i in range(idx, len(arr_times)):
            if cur >= arr_times[i]:
                wait_1.append(i)
                if i == len(arr_times) - 1:
                    idx = len(arr_times)
            else:
                idx = i
                break
        for i in range(len(r_time1)):
            if (not desk_1.get(i)) and wait_1:
                if i == a - 1:
                    answer_a.add(wait_1[0] + 1)
                desk_1[i] = [wait_1[0], cur + r_time1[i]]
                wait_1 = wait_1[1:]
        for i in range(len(r_time2)):
            if (not desk_2.get(i)) and wait_2:
                if i == b - 1:
                    answer_b.add(wait_2[0][2] + 1)
                desk_2[i] = [wait_2[0][2], cur + r_time2[i]]
                wait_2 = wait_2[1:]

        # calculate next time
        t1 = t2 = t3 = math.inf
        if idx < len(arr_times):
            t1 = arr_times[idx]
        if desk_1:
            tmp = sorted(desk_1.items(), key=lambda x: x[1][1])
            if tmp:
                t2 = tmp[0][1][1]
        if desk_2:
            tmp = sorted(desk_2.items(), key=lambda x: x[1][1])
            if tmp:
                t3 = tmp[0][1][1]

        # print("=======================================")
        # print("time:", cur, "waiting:", arr_times)
        # print("wait1:", wait_1)
        # print("wait2:", wait_2)
        # print("desk1:", desk_1)
        # print("desk2:", desk_2)
        # print("ts:", t1, t2, t3)
        # print("=================================")
        cur = min(t1, t2, t3)

    # print(answer_a)
    # print(answer_b)
    answer = answer_a.intersection(answer_b)
    if answer:
        return sum(answer)
    else:
        return -1


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n, m, k, a, b = map(int, input().split())
        arr_a = list(map(int, input().split()))
        arr_b = list(map(int, input().split()))
        times = list(map(int, input().split()))
        print("#%d %d" % (i, solution(arr_a, arr_b, times, a, b)))
