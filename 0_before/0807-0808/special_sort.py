def sorting(nums):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums
for tc in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    toggle = 1
    res = []
    nums = sorting(nums)
    print(nums)
    for i in range(10):
        if toggle == 1:
            res.append(nums[-1])
            del nums[-1]
            toggle = -1
        elif toggle == -1:
            res.append(nums[0])
            del nums[0]
            toggle = 1
    print('#{} {}'.format(tc+1, ' '.join(map(str, res))))