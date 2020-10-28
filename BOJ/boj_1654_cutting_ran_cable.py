import sys
sys.stdin = open('../input.txt', 'r')

K, N = map(int, input().split())
cables = []
for _ in range(K):
    cable = int(input())
    cables.append(cable)


start = 1
end = max(cables)

while start <= end:
    mid = (start + end) // 2
    cable_cnt = 0

    for cable in cables:
        cable_cnt += cable // mid
    if cable_cnt >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)