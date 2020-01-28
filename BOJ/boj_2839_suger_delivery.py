N = int(input())
res = 2000
cando = -1
for num_3 in range(int(N/3)+1):
    for num_5 in range(int(N/5)+1):
        if num_3 * 3 + num_5 * 5 == N and num_3 + num_5 < res:
            res = num_3 + num_5
            cando = 1

if cando == -1:
    res = -1

print(res)