def my_max(nums):
    maxnum = nums[0]
    for tmp in nums:
        if tmp > maxnum:
            maxnum = tmp
    return maxnum

def my_min(nums):
    minnum = nums[0]
    for tmp in nums:
        if tmp < minnum:
            minnum = tmp
    return minnum

for test in range(int(input())):
    num = int(input())
    nums = list(map(int, input().split()))
    print('#{} {}'.format(test+1, my_max(nums)-my_min(nums)))
