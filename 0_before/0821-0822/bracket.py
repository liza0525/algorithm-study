for test in range(int(input())):
    pcd = input()
    lst = ['(', ')', '{', '}']
    stack = []
    for ch in pcd:
        if ch in lst:
            if (stack and stack[-1] == '(' and ch == ')') or (stack and stack[-1] == '{' and ch == '}'):
                stack.pop()
            else:
                stack.append(ch)
        isEmpty = 0 if stack else 1
    print('#{} {}'.format(test+1, isEmpty))