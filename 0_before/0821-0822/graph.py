def dfsr(start):
    global result
    visited[start] =True
    for next in range(1, v+1):
        if info[start][next] and not visited[next]:
            if next == end:
                result = 1
                return
            dfsr(next)

for test in range(int(input())):
    v, e = map(int, input().split())
    info = [ [0]*(v+1) for i in range(v+1)]
    visited = [0] * (v+1)

    for i in range(e):
        a, b = map(int, input().split())
        info[a][b] = 1

    start, end = map(int, input().split())
    result = 0
    dfsr(start)
    print('#{} {}'.format(test+1, result))