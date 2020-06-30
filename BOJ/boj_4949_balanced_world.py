import sys
sys.stdin = open('../input.txt', 'r')

bracket = ['[', ']', '(', ')']

while True:
    stack = list()
    res = ''
    line = input()
    if line == '.':
        break
    for ch in line:
        if ch not in bracket:
            continue
        if ch =='(' or ch =='[':
            stack.append(ch)
        else:
            if not stack:
                res = 'no'
                break
            if ch == ')' and stack[-1] == '(':
                stack.pop()
            elif ch == ']' and stack[-1] == '[':
                stack.pop()
            else:
                res = 'no'
                break
    else:
        if not stack:
            res = 'yes'
        else:
            res = 'no'

    print(res)