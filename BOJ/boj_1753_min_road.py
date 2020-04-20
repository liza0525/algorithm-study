# reference : https://hjp845.tistory.com/44
import sys
import heapq
sys.stdin = open('../input.txt', 'r')
inpu = sys.stdin.readline
INF = 999999999

def dijkstra(v, start, g):
    dist = [INF] * (V + 1)
    dist[start] = 0
    q = []
    heapq.heappush(q, [0, start])
    while q:
        cost, loc = heapq.heappop(q)
        for l, c in g[loc]:
            c += cost
            if c < dist[l]:
                dist[l] = c
                heapq.heappush(q, [c, l])
    return dist[1:]


V, E = map(int, inpu().split())
K = int(inpu())
G = [[] for i in range(V + 1)]
for i in range(E):
    u, v, w = map(int, inpu().split())
    G[u].append([v, w])

for x in dijkstra(V, K, G):
    print(x if x != INF else "INF")


# def djikstra(start):
#     cand = []
#     for idx, dist in info[start]:
#         if total_dist[idx] == 1e9:
#             total_dist[idx] = min(total_dist[start] + dist, total_dist[idx])
#             # if total_dist[idx] < cand:
#             cand.append(total_dist[idx])
#     return cand
#
#
# V, E = map(int, input().split())
# K = int(input())
#
# info = dict()
#
# for _ in range(E):
#     s, e, d = map(int, input().split())
#     if s not in info.keys():
#         info.update({s: [(e, d)]})
#     else:
#         info[s].append((e, d))
# total_dist = [1e9] * (V+1)
#
# start = K
# total_dist[start] = 0
#
# while True:
#     cand = djikstra(start)
#     while cand:
#         start = total_dist.index(min(cand))
#         if start in info.keys():
#             break
#         cand.remove(min(cand))
#     if not cand:
#         break
#
# for res in total_dist[1:]:
#     if res == 1e9:
#         res = 'INF'
#     print(res)