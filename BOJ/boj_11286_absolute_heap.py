import sys
sys.stdin = open('../input.txt', 'r')
import heapq

N = int(input())
num_heap = []

for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if num_heap:
            print(heapq.heappop(num_heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(num_heap, (abs(num), num))
