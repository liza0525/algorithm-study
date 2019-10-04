import sys
sys.stdin = open("../inputdata/swea_5202.txt", "r")

for test in range(int(input())):
    n = int(input())
    trucks = [list(map(int, input().split())) for _ in range(n)]
    limit, res = 24, 0
    while limit > 0:
        tmp = []
        for truck in trucks:
            if truck[1] <= limit:
                tmp.append(truck)
        if not tmp:
            break
        pick = max(tmp)
        limit = pick[0]
        trucks.pop(trucks.index(pick))
        res += 1

    print('#{} {}'.format(test+1, res))
