import sys
sys.stdin = open('../input.txt', 'r')

N = int(input())
nums = list(map(int, input().split()))
if 1 in nums:
    nums.remove(1)
res = 0
for num in nums:
    for i in range(2, num//2+1):
        if num % i == 0:
            break
    else:
        # print(num)
        res += 1

print(res)