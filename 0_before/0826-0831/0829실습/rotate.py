import sys
sys.stdin = open('rotate.txt','r')

for test in range(int(input())):
    n, m = map(int,input().split())
    nums = list(map(int, input().split()))

    for i in range(m):
        nums.append(nums.pop(0))
    print('#{} {}'.format(test+1, nums[0]))