import sys


def solution(cmds):
    arr = []
    answer = []
    for cmd in cmds:
        flag = cmd[0]
        if flag == 1:
            arr.append((cmd[1], cmd[2]))
        elif flag == 2:
            target = cmds[cmd[1]-1]
            if (target[1], target[2]) in arr:
                arr.remove((target[1], target[2]))
        else:
            if not arr:
                answer.append("NO")
            else:
                max_val = 0
                for elem in arr:
                    max_val = max(max_val, cmd[1]*elem[0] + elem[1])
                answer.append(str(max_val))
    return "\n".join(answer)


if __name__ == "__main__":
    sys.stdin = open("input", "r")
    tests = int(input())
    for i in range(1, tests+1):
        n = int(input())
        cmds = [list(map(int, (input().split()))) for _ in range(n)]
        print("#%d\n%s" % (i, solution(cmds)))
