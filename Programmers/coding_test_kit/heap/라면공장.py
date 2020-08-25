import heapq
def solution(stock, dates, supplies, k):
    answer = 0
    today = 0
    maxheap = []
    while stock < k:
        for i in range(today, len(dates)):
            if dates[i] > stock:
                break
            heapq.heappush(maxheap, -supplies[i])
            today = i + 1
        stock += -heapq.heappop(maxheap)
        answer += 1
    return answer