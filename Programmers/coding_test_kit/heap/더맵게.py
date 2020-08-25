import heapq

def solution(scoville, K):
    answer = 0
    minheap = []
    for itm in scoville:
        heapq.heappush(minheap, itm)
    while True:
        if minheap[0] >= K:
            break
        if len(minheap) < 2 and minheap[0] < K:
            answer = -1
            break
        item1 = heapq.heappop(minheap)
        item2 = heapq.heappop(minheap)
        heapq.heappush(minheap, item1 + item2 * 2)
        answer += 1

    return answer