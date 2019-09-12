def e_sort(elements):
    res=[]
    res.append(elements.pop())
    while elements:
        for i in range(len(elements)):
            if res[0][0] == elements[i][1]:
                res.insert(0, elements.pop(i))
                break
            elif res[-1][1] == elements[i][0]:
                res.append(elements.pop(i))
                break
    return res

for tc in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    elements = []
    for i in range(0,len(nums),2):
        elements.append([nums[i],nums[i+1]])
    
    elements = e_sort(elements)
    res_s = ''
    print('#{}'.format(tc+1), end=' ')
    for x,y in elements:
        print(x,y, end=' ')
    print()
