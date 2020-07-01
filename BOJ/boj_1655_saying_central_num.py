import sys
sys.stdin = open('../input.txt', 'r')
import heapq

N = int(sys.stdin.readline())
minheap, maxheap = [],[]
for _ in range(N):
    num = int(sys.stdin.readline())

    if len(minheap) == len(maxheap):
        heapq.heappush(maxheap, -num)
    else:
        heapq.heappush(minheap, num)

    if minheap and -minheap[0] > maxheap[0]:
        mintop = heapq.heappop(minheap)
        maxtop = heapq.heappop(maxheap)
        heapq.heappush(maxheap, -mintop)
        heapq.heappush(minheap, -maxtop)

    print(-maxheap[0])