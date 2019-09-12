def sortlist(heights):
    cnt = [0 for i in range(len(heights))]
    for i in range(len(heights)-1):
        for j in range(i+1, len(heights)):
            if heights[i] > heights[j]:
                heights[i], heights[j] = heights[j], heights[i]
    return heights

for test in range(10):
    dump = int(input())
    heights = list(map(int, input().split()))
    for i in range(dump):
        heights = sortlist(heights)
        heights[0] += 1
        heights[99] -= 1
    heights = sortlist(heights)
    print(heights)
    print('#{} {}'.format(test+1, heights[99]-heights[0]))
