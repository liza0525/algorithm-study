def binarySearch(page, goal):
    first_p, last_p, cnt = 1, page, 0
    while first_p != goal and last_p != goal:
        md_p = int((first_p+last_p)/2)
        if goal >= md_p:
            first_p = md_p
        else:
            last_p = md_p
        cnt += 1
    return cnt

for tc in range(int(input())):
    p, a, b = map(int, input().split())
    cnt_a, cnt_b = binarySearch(p,a), binarySearch(p,b)
    if cnt_a < cnt_b:
        print('#{} A'.format(tc+1))
    elif cnt_a > cnt_b:
        print('#{} B'.format(tc+1))
    else:
        print('#{} 0'.format(tc+1))