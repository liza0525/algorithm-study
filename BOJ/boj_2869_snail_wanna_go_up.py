import sys
sys.stdin = open('../input.txt', 'r')

A, B, V = map(int, input().split())

days = 0
diff = A - B

days = (V - B) / diff

print(int(days) if days == int(days) else int(days+1))