import sys
sys.stdin = open('../input.txt', 'r')

N = int(input())
Nlen = len(str(N))
for i in range(1, N):
    total = i
    num = i
    for j in range(Nlen, -1, -1):
        temp = (num // (10 ** j))
        total += temp
        num = num - temp * (10 ** j)
    if total == N:
        print(i)
        break
else:
    print(0)
