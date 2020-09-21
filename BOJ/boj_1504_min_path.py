import sys
import heapq
sys.stdin = open('../input.txt', 'r')


def dijstra(start, end):
    dists = [float('inf') for _ in range(N)]
    dists[start] = 0
    queue = []
    heapq.heappush(queue, [dists[start], start])

    while queue:
        curr_dist, curr_node = heapq.heappop(queue)

        if dists[curr_node] < curr_dist:
            continue

        for next_node in range(N):
            total_dist = curr_dist + graph[curr_node][next_node]
            if total_dist < dists[next_node]:
                dists[next_node] = total_dist
                heapq.heappush(queue, [dists[next_node], next_node])
    return dists[end]


N, E = map(int, input().split())

graph = [[float('inf') for _ in range(N)] for _ in range(N)]
for _ in range(E):
    first_node, second_node, weight = map(int, input().split())
    graph[first_node-1][second_node-1], graph[second_node-1][first_node-1] = weight, weight

v1, v2 = map(int, input().split())
v1 -= 1
v2 -= 1

start_to_v1 = dijstra(0, v1)
start_to_v2 = dijstra(0, v2)
v1_to_end = dijstra(v1, N-1)
v2_to_end = dijstra(v2, N-1)
v1_to_v2 = dijstra(v1, v2)


path1 = start_to_v1 + v2_to_end
path2 = start_to_v2 + v1_to_end

if v1_to_v2 == float('inf'):
    print(-1)
elif path1 < path2:
    print(path1 + v1_to_v2) if path1 != float('inf') else -1
else:
    print(path2 + v1_to_v2) if path2 != float('inf') else -1
