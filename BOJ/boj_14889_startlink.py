def power(arr):
    p = 0
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            p += table[arr[i]][arr[j]] + table[arr[j]][arr[i]]
    return p


def combi(arr, d, next):
    global res
    if d == int(n/2):
        g1 = arr[:]
        g2 = list(set(members)-set(g1))
        temp_res = abs(power(g1) - power(g2))
        if temp_res < res:
            res = temp_res
    else:
        for i in range(next, n):
            temp = arr[:]
            temp.append(i)
            combi(temp, d+1, i+1)
            temp.pop()


n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]
members = [i for i in range(n)]
res = 987654321

combi([], 0, 0)

print(res)