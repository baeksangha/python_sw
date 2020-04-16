import sys


def solution(input):
    answer = 0
    croak = {"c": 0, "r": 0, "o": 0, "a": 0, "k": 0}
    alpha = ["c", "r", "o", "a", "k"]
    for ch in input:
        if ch == "c":
            croak[ch] += 1
        else:
            for i in range(1, 5):
                if alpha[i] == ch:
                    if croak[alpha[i-1]] > 0:
                        croak[alpha[i-1]] -= 1
                        if ch != "k":
                            croak[alpha[i]] += 1
                    else:
                        return -1
                    break
        answer = max(answer, sum(croak.values()))

    for elem in croak.values():
        if elem != 0:
            return -1

    return answer


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        ch = input()
        print("#%d %d" % (i, solution(ch)))
