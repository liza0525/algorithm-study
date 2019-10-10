import sys
sys.stdin = open('input.txt', 'r')

for test in range(10):
    N = int(input())
    visited = []
    res = ''
    tree_info = [0]
    for _ in range(N):
        tmp = list(input().split())
        tree_info.append(tmp)

    i = 1
    stack_ch = [tree_info[i][1]]
    stack_n = [i]
    visited.append(i)

    while len(visited) < N:
        if len(tree_info[i]) >= 3:
            i = int(tree_info[i].pop(2))
            stack_ch.append(tree_info[i][1])
            stack_n.append(i)
            visited.append(i)
        elif len(tree_info[i]) == 2:
            res += stack_ch.pop()
            i = stack_n.pop()

    print('#{} {}'.format(test+1, res))