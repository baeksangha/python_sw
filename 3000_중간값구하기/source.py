import sys
import heapq


def solution(s, nums):
    max_heap = []
    min_heap = []
    heapq.heappush(max_heap, -s)
    answer = 0
    mod = 20171109
    for num in nums:
        for n in num:
            if -max_heap[0] >= n:
                tmp = -heapq.heappop(max_heap)
                heapq.heappush(min_heap, tmp)
                heapq.heappush(max_heap, -n)
            else:
                heapq.heappush(min_heap, n)
        if len(max_heap) < len(min_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
        answer = (answer - max_heap[0]) % mod

    return answer


if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n, a = map(int, input().split())
        nums = [list(map(int, input().split())) for _ in range(n)]
        print("#%d %d" % (i, solution(a, nums)))
