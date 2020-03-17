N =int(input())

nums = [list(map(int, input().split())) for _ in range(N)]
nums = list(map(list, zip(*nums)))
res = 0
list1, list2 = dict(), dict()
for i in nums[0]:
    for j in nums[1]:
        if i+j not in list1.keys():
            list1[i+j] = 1
        else:
            list1[i+j] += 1

for i in nums[2]:
    for j in nums[3]:
        if i+j not in list2.keys():
            list2[i+j] = 1
        else:
            list2[i+j] += 1


for i in list1.keys():
    if -i in list2.keys():
        res += list1[i] * list2[-i]

print(res)