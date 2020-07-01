import sys
sys.stdin = open('../input.txt', 'r')
import heapq

N = int(sys.stdin.readline())
q = list()
for _ in range(N):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(q, num)
    else:
        try:
            print(heapq.heappop(q))
        except:
            print(0)