import sys
sys.stdin = open('../input.txt', 'r')

N, C = map(int, input().split())
houses = []
for _ in range(N):
    houses.append(int(input()))
houses.sort()

# 설치 가능한 거리
min_dist = 1
max_dist = houses[-1] - houses[0]
dist = 0
while min_dist <= max_dist:
    mid = (max_dist + min_dist) // 2
    start = houses[0]
    cnt = 1

    for i in range(1, N):
        d = houses[i] - start
        if mid <= d:
            cnt += 1
            start = houses[i]

    if cnt >= C:
        dist = mid
        min_dist = mid + 1
    else:
        max_dist = mid - 1

print(dist)