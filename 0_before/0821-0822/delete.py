for test in range(int(input())):
    chs = input()
    stack = []
    for ch in chs:
        if not stack or stack[-1] != ch:
            stack.append(ch)
        elif stack[-1] == ch:
            stack.pop()

    print('#{} {}'.format(test+1, len(stack)))