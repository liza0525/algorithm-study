import sys
sys.stdin = open('../input.txt', 'r')

N = int(input())
time_list = [tuple(map(int, input().split())) for _ in range(N)]
time_list = sorted(time_list, key=lambda x: (x[1], x[0]))

cnt = 1
start_time, end_time = time_list[0]
for next_start_time, next_end_time in time_list[1:]:
    if next_start_time >= end_time:
        start_time, end_time = next_start_time, next_end_time
        cnt += 1

print(cnt)
