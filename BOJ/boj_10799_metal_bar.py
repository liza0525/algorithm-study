import sys
sys.stdin = open('../input.txt', 'r')

brackets = input()
bar_cnt = 0
stack = []
for idx in range(len(brackets)):
    if brackets[idx] == '(':
        stack.append(brackets[idx])
    elif brackets[idx] == ')':
        stack.pop()
        if brackets[idx-1] == '(':
            bar_cnt += len(stack)
        elif brackets[idx-1] == ')':
            bar_cnt += 1

print(bar_cnt)