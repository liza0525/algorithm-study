for test in range(10):
    N = int(input())
    visited = []
    res = ''
    tree_info = [0]
    for _ in range(N):
        tmp = list(input().split())
        tree_info.append(tmp)

    i = 1
    stack = [(i, tree_info[i][1])]
    visited.append(i)

    while len(visited) < N or stack:
        if len(tree_info[i]) >= 3:
            i = int(tree_info[i].pop(2))
            stack.append((i, tree_info[i][1]))
            visited.append(i)
        elif len(tree_info[i]) == 2:
            tmp_i, tmp_ch = stack.pop()
            i = tmp_i
            res += tmp_ch

    print('#{} {}'.format(test+1, res))