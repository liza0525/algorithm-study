import sys
sys.stdin = open("../inputdata/swea_5201.txt", "r")

for test in range(int(input())):
    n, m = map(int, input().split())
    wl = list(map(int, input().split()))
    tl = list(map(int, input().split()))

    res = 0

    while wl and tl:
        max_t = max(tl)
        max_w = max(wl)

        if max_w > max_t:
            wl.pop(wl.index(max_w))
        else:
            res += max_w
            wl.pop(wl.index(max_w))
            tl.pop(tl.index(max_t))

    print('#{} {}'.format(test+1, res))