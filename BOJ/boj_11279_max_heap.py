import sys
sys.stdin = open('../input.txt', 'r')
import heapq

N = int(sys.stdin.readline())
queue = list()
for _ in range(N):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(queue, -num)
    else:
        try:
            print(-1 * heapq.heappop(queue))
        except:
            print(0)