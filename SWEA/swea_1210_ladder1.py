for _ in range(10):
    test = int(input())
    ground = [list(map(int, input().split())) for _ in range(100)]
    ladder_col = [i for i in range(100) if ground[0][i] == 1]

    for i in range(100):
        if ground[99][i] == 2:
            now_idx = ladder_col.index(i)
            break

    for row in range(99, -1, -1):
        if ladder_col[now_idx] != 0 and ground[row][ladder_col[now_idx] - 1] == 1:
            now_idx -= 1
        elif ladder_col[now_idx] != 99 and ground[row][ladder_col[now_idx] + 1] == 1:
            now_idx += 1

    print('#{} {}'.format(test, ladder_col[now_idx]))