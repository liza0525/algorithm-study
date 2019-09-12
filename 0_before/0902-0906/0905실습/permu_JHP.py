def permu(arr, depth):
    global count
    if depth == M:
        count += 1
        print('p', count, ':', arr)
    else:
        for i in range(N):
            if not visited[i]:
                ar = arr[:]
                visited[i] = 1
                ar.append(i)
                permu(ar, depth + 1)
                visited[i] = 0


def permu_repet(arr, depth):
    global count
    if depth == M:
        count += 1
        print('pr', count, ':', arr)
    else:
        for i in range(N):
            ar = arr[:]
            ar.append(i)
            permu_repet(ar, depth + 1)


def combi(arr, depth, last):
    global count
    if depth == M:
        count += 1
        print('c', count, ':', arr)
    else:
        for i in range(last + 1, N):
            ar = arr[:]
            ar.append(i)
            combi(ar, depth + 1, i)


def combi_repet(arr, depth, last):
    global count
    if depth == M:
        count += 1
        print('cr', count, ':', arr)
    else:
        for i in range(last, N):
            ar = arr[:]
            ar.append(i)
            combi_repet(ar, depth + 1, i)


# N, M = map(int, input().split())
N, M = 6,3
count = 0
visited = [0] * N
combi([], 0, 0)
# permu([], 0)
# combi_repet([], 0, 0)
# permu_repet([], 0)