import sys
sys.stdin = open('input.txt', 'r')

for test in range(int(input())):
    n, b = map(int, input().split())
    heights = list(map(int, input().split()))
    differs = []
    for i in range(1 << n):
        total = 0
        for j in range(n+1):
            if i & (1 << j):
                total += heights[j]
                if total >= b:
                    differs.append(total-b)
                    break

    print('#{} {}'.format(test+1, min(differs)))