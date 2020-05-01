import sys


def solution(n, matrix):

    for i in range(n):
        output = ""
        for j in range(n-1, -1, -1):
            output += str(matrix[j][i])
        output += " "
        for j in range(n-1, -1, -1):
            output += str(matrix[n-i-1][j])
        output += " "
        for j in range(n):
            output += str(matrix[j][n-i-1])
        print(output)

    return None


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        n = int(input())
        matrix = [list(map(int, input().split())) for _ in range(n)]
        print("#%d" % i)
        solution(n, matrix)
