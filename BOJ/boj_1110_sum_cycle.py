import sys
sys.stdin = open('../input.txt', 'r')

start = num = int(input())
cnt = 0
while True:
    new_num = num // 10 + num % 10
    num = num % 10 * 10 + new_num % 10
    cnt += 1
    if start == num:
        break

print(cnt)