import sys
sys.stdin = open('../input.txt', 'r')

# wine = int(input())
# wine_capa = [0]
# result = [0 for _ in range(wine + 1)]
#
# for _ in range(wine):
#     wine_capa.append(int(input()))
#
# for i in range(1, wine + 1):
#     if i == 1:
#         result[1] = wine_capa[1]
#     elif i == 2:
#         result[2] = wine_capa[1] + wine_capa[2]
#     else:
#         result[i] = max(result[i-3] + wine_capa[i-1] + wine_capa[i], result[i-2] + wine_capa[i], result[i-1])
#
# print(result)
# print(result[i])



N = int(input())
wines = [0 for _ in range(N)]
sum_wines = [0 for _ in range(N)]

for i in range(N):
    wines[i] = int(input())

if N >= 1:
    sum_wines[0] = wines[0]
if N >= 2:
    sum_wines[1] = wines[0] + wines[1]
if N >= 3:
    for idx in range(2, N):
        sum_wines[idx] = max(sum_wines[idx-3] + wines[idx-1] + wines[idx], sum_wines[idx-2] + wines[idx], sum_wines[idx-1])

# print(sum_wines)
print(max(sum_wines))