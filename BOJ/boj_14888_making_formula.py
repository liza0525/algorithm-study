import sys
sys.stdin = open('../input.txt', 'r')

def operating(res, d):
    global min_num, max_num
    if d == N-1:
        if res < min_num:
            min_num = res
        if res > max_num:
            max_num = res
    else:
        for i in range(4):
            if operator[i]:
                d += 1
                operator[i] -= 1
                temp = res
                if i == 0:
                    res += nums[d]
                elif i == 1:
                    res -= nums[d]
                elif i == 2:
                    res *= nums[d]
                elif i == 3:
                    res = int(res / nums[d])
                operating(res, d)
                d -= 1
                operator[i] += 1
                res = temp


N = int(input())
nums = list(map(int, input().split()))
operator = list(map(int, input().split()))
max_num = -1000000000
min_num = 1000000000

operating(nums[0], 0)

print(max_num)
print(min_num)
