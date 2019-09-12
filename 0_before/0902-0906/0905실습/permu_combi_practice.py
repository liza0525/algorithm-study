def combi(arr, depth, num):
    if depth == m:
        print(arr)
    else:
        for i in range(num, len(ch)):
            tmp = arr[:]
            tmp.append(ch[i])
            combi(tmp, depth+1, i+1)


m = 2
ch = ['a', 'b', 'c', 'd']
combi([], 0, 0)
res = []
print(res)