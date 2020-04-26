import sys


def solution(binary, tenary):
    for i in range(len(binary)):
        if binary[i] == '0':
            token = binary[:i] + "1" + binary[i+1:]
        else:
            token = binary[:i] + "0" + binary[i+1:]
        bin_token = int(token, 2)
        for j in range(len(tenary)):
            if tenary[j] == '0':
                ten_token1 = int(tenary[:j]+"1"+tenary[j+1:], 3)
                ten_token2 = int(tenary[:j]+"2"+tenary[j+1:], 3)
                if bin_token == ten_token1 or bin_token == ten_token2:
                    return bin_token
            elif tenary[j] == '1':
                ten_token1 = int(tenary[:j] + "0" + tenary[j+1:], 3)
                ten_token2 = int(tenary[:j] + "2" + tenary[j+1:], 3)
                if bin_token == ten_token1 or bin_token == ten_token2:
                    return bin_token
            else:
                ten_token1 = int(tenary[:j] + "0" + tenary[j+1:], 3)
                ten_token2 = int(tenary[:j] + "1" + tenary[j+1:], 3)
                if bin_token == ten_token1 or bin_token == ten_token2:
                    return bin_token
    return -1


if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        binary = input()
        tenary = input()
        print("#%d %d" % (i, solution(binary, tenary)))
