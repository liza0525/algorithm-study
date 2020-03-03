N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

total = N

for i in range(N):
    if A[i] > B:
        A[i] -= B
    else:
        A[i] = 0

for i in range(N):
    if A[i] and A[i] % C != 0:
        total += (A[i] // C + 1)
    else:
        total += (A[i] // C)

print(total)
