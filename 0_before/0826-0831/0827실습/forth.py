def calc(a, b, ch):
    if ch == '+':
        return a+b
    elif ch == '-':
        return a-b
    elif ch == '*':
        return a*b
    elif ch == '/':
        return int(a/b)

for test in range(int(input())):
    postfix = list(map(str, input().split()))
    stack = []

    for ch in postfix:
        if ch.isdigit():
            stack.append(int(ch))
        elif ch == '.':
            if len(stack) == 1:
                print('#{} {}'.format(test+1, stack[0]))
            else:
                print('#{} error'.format(test+1))
        else:
            if len(stack) > 1:
                b = stack.pop()
                a = stack.pop()
                stack.append(calc(a, b, ch))
            else:
                print('#{} error'.format(test+1))
                break