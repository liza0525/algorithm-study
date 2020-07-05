import sys
sys.stdin = open('../input.txt', 'r')

N = int(input())
fibo = [0] * N
if N == 0 or N == 1:
    print(1)
else:
    fibo[0], fibo[1] = 1, 1
    for i in range(2, N):
        fibo[i] = fibo[i-1] + fibo[i-2]
    print(fibo[N-1])