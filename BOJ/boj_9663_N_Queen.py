def n_queen(arr):
    global count
    if len(arr) == N:
        count += 1
    else:
        for cand in range(N):
            if cand in arr:
                continue
            for i in range(len(arr)):
                if abs(cand - arr[i]) == len(arr) - i:
                    break
            else:
                arr.append(cand)
                n_queen(arr)
                arr.pop()


N = int(input())
count = 0

for i in range(N):
    n_queen([i])

print(count)