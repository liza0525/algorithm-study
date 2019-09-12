t = int(input())

for tc in range(t):
    n, k = map(int, input().split())
    base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    cnt = 0
    basel = len(base)
    for i in range(1<<basel):
        tmplist = []
        for j in range(basel):
            if i & (1 << j): 
                tmplist.append(base[j])
        if len(tmplist) == n and sum(tmplist) == k:
            cnt += 1
    print('#{} {}'.format(tc+1, cnt))