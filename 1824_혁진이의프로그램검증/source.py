import sys


def solution(r, c, board, x, y, direction, route, value):
    answer = "No"
    compass = {'l': [0, -1], 'r': [0, 1], 'u': [-1, 0], 'd': [1, 0]}
    dir = direction
    while True:
        token = board[x][y]
        if '0' <= token <= '9':
            value = int(token)
        elif token in ['<', '>', '^', 'v']:
            if token == '<':
                dir = 'l'
            elif token == '>':
                dir = 'r'
            elif token == '^':
                dir = 'u'
            else:
                dir = 'd'
        elif token == '_':
            if value == 0:
                dir = 'r'
            else:
                dir = 'l'
        elif token == '|':
            if value == 0:
                dir = 'd'
            else:
                dir = 'u'
        elif token == '+':
            value = (value + 1) % 16
        elif token == '-':
            value = (value - 1) % 16
        elif token == '?':
            for direction in ['u', 'r', 'd', 'l']:
                new_x, new_y = ((x + compass[direction][0]) % r), ((y + compass[direction][1]) % c)
                ret = solution(r, c, board, new_x, new_y, direction, route, value)
                if ret == "Yes":
                    return "Yes"
            return "No"
        elif token == '@':
            answer = "Yes"
            break
        rec = (x, y, value, dir)
        if rec in route:
            break
        else:
            route.add((x, y, value, dir))
        x, y = ((x + compass[dir][0]) % r), ((y + compass[dir][1]) % c)
    return answer


if __name__ == "__main__":
    sys.stdin = open('input', 'r')
    tests = int(input())
    for i in range(1, tests+1):
        r, c = map(int, input().split())
        board = [list(input()) for _ in range(r)]
        print("#%d %s" % (i, solution(r, c, board, 0, 0, 'r', set(), 0)))
