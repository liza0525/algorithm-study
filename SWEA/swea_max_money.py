for test in range(int(input())):
    money, n = input().split()
    nums = [int(ch) for ch in money]
    n = int(n)
    max_money = 0
    cnt = 0
    i = 0
    while cnt < n:
        if nums.count(max(nums)) == len(nums) - 1:
            break
        if nums.count(max(nums)) >= n:
            if max(nums) not in nums[:n]:
                nums = sorted(nums[:n])+nums[n:]
        if i == len(nums) - 2:
            nums[-1], nums[-2] = nums[-2], nums[-1]
            cnt += 1
        else:
            if nums[i] != max(nums[i:]):
                tmp = nums[i+1:]
                if tmp.count(max(tmp)) > 1:
                    mi = len(nums) - tmp[::-1].index(max(tmp[::-1])) - 1
                else:
                    mi = tmp.index(max(tmp)) + (i + 1)
                nums[i], nums[mi] = nums[mi], nums[i]
                cnt += 1
            i += 1

    for i in range(len(nums)):
        max_money += nums[len(nums) - 1 - i] * (10 ** i)
    print('#{} {}'.format(test + 1, max_money))