import sys


def solution(s, words):
    keypad = ['0', '0', "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    answer = 0
    for word in words:
        if len(word) != len(s):
            continue
        is_success = 1
        for i in range(len(word)):
            if word[i] not in keypad[int(s[i])]:
                is_success = 0
                break
        if is_success:
            answer += 1
    return answer


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        s, n = input().split()
        words = input().split()
        print("#%d %d" % (i, solution(s, words)))
