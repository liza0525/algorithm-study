import sys
sys.stdin = open('../input.txt', 'r')

N = int(input())
res = ''
for _ in range(N):
    line = input()
    stack = list()
    for b in line:
        if b == '(':
            stack.append(b)
        else:
            if not stack:
                res = 'NO'
                break
            if stack[-1] == '(':
                stack.pop()
            else:
                res = 'NO'
                break
    else:
        if not stack:
            res = 'YES'
        else:
            res = 'NO'

    print(res)