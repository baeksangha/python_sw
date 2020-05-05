import sys
import math


def get_index(words, query, flag):
    left, right = 0, len(words)
    if flag == 0:
        index = math.inf
    else:
        index = -1

    s_len = query.index("?")
    head = query[:s_len]
    while left <= right and (left + right) // 2 < len(words):

        mid = (left + right) // 2
        target = words[mid]
        if len(target) > len(query):
            right = mid - 1
        elif len(target) < len(query):
            left = mid + 1
        else:
            if head > target[:s_len]:
                left = mid + 1
            elif head < target[:s_len]:
                right = mid - 1
            else:
                if flag == 0:
                    index = min(index, mid)
                    right = mid - 1
                else:
                    index = max(index, mid)
                    left = mid + 1
    return index


def solution(words, queries):
    q_origin = queries[:]
    answer = []
    answer_dict = {}
    words_reverse = [x[::-1] for x in words]

    words.sort(key=lambda x: (len(x), x))
    words_reverse.sort(key=lambda x: (len(x), x))
    queries.sort(key=lambda x: (len(x), x))

    prefix, suffix = [], []
    for query in queries:
        if query[0] == '?':
            prefix.append(query[::-1])
        else:
            suffix.append(query)
    for query in suffix:
        l_idx = get_index(words, query, 0)
        r_idx = get_index(words, query, 1)
        if l_idx == math.inf or r_idx == -1:
            answer_dict[query] = 0
        else:
            answer_dict[query] = r_idx - l_idx + 1
    for query in prefix:
        l_idx = get_index(words_reverse, query, 0)
        r_idx = get_index(words_reverse, query, 1)
        if l_idx == math.inf or r_idx == -1:
            answer_dict[query[::-1]] = 0
        else:
            answer_dict[query[::-1]] = r_idx - l_idx + 1
    for query in q_origin:
        answer.append(answer_dict[query])
    return answer


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    words = input().split()
    queries = input().split()
    solution(words, queries)