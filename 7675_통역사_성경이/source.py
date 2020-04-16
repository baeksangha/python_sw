import sys


def solution(sentences):
    answer = []
    cnt = 0
    sentences = (" ".join(sentences)).split(" ")
    for s in sentences:
        if s[0].isupper():
            if len(s) == 1:
                cnt += 1
            else:
                if s[-1] == '.' or s[-1] == '?' or s[-1] == '!':
                    if (s[1:-1].islower() and s[1:-1].isalpha()) or not s[1:-1]:
                        cnt += 1
                elif s[1:].islower() and s[1:].isalpha():
                    cnt += 1
        if s[-1] == '.' or s[-1] == '?' or s[-1] == '!':
            answer.append(str(cnt))
            cnt = 0

    return answer


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n = int(input())
        sentences = []
        cnt = 0
        while cnt != n:
            sentence = input()
            sentences.append(sentence)
            cnt += sentence.count(".") + sentence.count("?") + sentence.count("!")
        ret = solution(sentences)
        print("#%d" % i, " ".join(ret))
