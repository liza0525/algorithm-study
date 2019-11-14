def score(arr):
    s = 0
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            s += table[arr[i]][arr[j]] + table[arr[j]][arr[i]]
    return s


def combi(arr, d, next):
    global group1,group2, res
    if d == int(N/2):
        group1 = arr[:]
        group2 = list(set(food) - set(arr))
        temp_res = abs(score(group1) - score(group2))
        if temp_res < res:
            res = temp_res
    else:
        for i in range(next, N):
            temp = arr[:]
            temp.append(i)
            combi(temp, d+1, i+1)
            temp.pop()


for test in range(int(input())):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    food = [i for i in range(N)]
    group1, group2 = [], []
    res = 987654321

    combi([], 0, 0)

    print('#{} {}'.format(test+1, res))