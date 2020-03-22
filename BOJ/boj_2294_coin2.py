N, K = map(int, input().split())
values = sorted([int(input()) for _ in range(N)])
# print(values)
nums = [100001] * (K+1)
nums[0] = 0

for value in values:
    for j in range(value, K+1):
        nums[j] = min(nums[j], nums[j-value]+1)

if nums[-1] != 100001:
    print(nums[-1])
else:
    print(-1)
