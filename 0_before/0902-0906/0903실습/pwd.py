import sys
sys.stdin = open('pwd.txt', 'r')

for test in range(int(input())):
    n, m, k = map(int, input().split())
    nums = list(map(int, input().split()))
    idx = 0

    for i in range(k):
        idx += m
        if idx > len(nums):
            idx -= len(nums)
        nums.insert(idx, 0)
        pstidx = idx+1 if idx < len(nums)-1 else 0
        preidx = idx-1
        nums[idx] = nums[preidx]+nums[pstidx]

    print('#{} {}'.format(test+1, ' '.join(map(str, list(reversed(nums))[:10]))))