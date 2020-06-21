import sys
sys.stdin = open('../input.txt', 'r')

N = int(input())
M = int(input())

print(N * (M % 10))
print(N * ((M // 10) % 10))
print(N * (M // 100))
print(N*M)