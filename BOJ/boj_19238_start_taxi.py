import sys
sys.stdin = open('../input.txt', 'r')

import collections
import heapq

deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def is_field(r, c):
    return 0 <= r < N and 0 <= c < N


def find_destination(taxi_r, taxi_c, person_num):
    global fuel
    queue = collections.deque()
    queue.append((taxi_r, taxi_c))
    dest_r, dest_c = destinations[person_num]
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[taxi_r][taxi_c] = 1
    distance = 0

    while queue:
        is_arrive = False
        temp = queue
        queue = collections.deque()
        while temp:
            now_r, now_c = temp.popleft()
            for delta_r, delta_c in deltas:
                next_r, next_c = now_r + delta_r, now_c + delta_c
                if not is_field(next_r, next_c): continue
                if ground[next_r][next_c] == 1: continue
                if visited[next_r][next_c]: continue
                if next_r == dest_r and next_c == dest_c:
                    is_arrive = True
                    break
                queue.append((next_r, next_c))
                visited[next_r][next_c] = True

        fuel -= 1
        distance += 1

        if fuel == 0:
            if not is_arrive:
                fuel = -1
                return

        if is_arrive:
            break

    if not is_arrive:
        fuel = -1
        return

    fuel += distance * 2
    ground[taxi_r][taxi_c] = 0


def move(taxi_r, taxi_c):
    global fuel
    queue = collections.deque()
    queue.append((taxi_r, taxi_c))
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[taxi_r][taxi_c] = 1
    cand = []

    while queue and destinations:
        is_same = False
        temp = queue
        queue = collections.deque()
        while temp:
            now_r, now_c = temp.popleft()
            if ground[now_r][now_c] > 1:
                is_same = True
                heapq.heappush(cand, (now_r, now_c, ground[now_r][now_c]))
                break
            else:
                for delta_r, delta_c in deltas:
                    next_r, next_c = now_r + delta_r, now_c + delta_c
                    if not is_field(next_r, next_c): continue
                    if ground[next_r][next_c] == 1: continue
                    if visited[next_r][next_c]: continue
                    queue.append((next_r, next_c))
                    visited[next_r][next_c] = True
                    if ground[next_r][next_c] > 1:
                        heapq.heappush(cand, (next_r, next_c, ground[next_r][next_c]))

        if not is_same:
            fuel -= 1

        if fuel == 0:
            fuel = -1
            break

        if cand:
            taxi_r, taxi_c, person_num = heapq.heappop(cand)
            find_destination(taxi_r, taxi_c, person_num)

            if fuel == -1:
                break

            taxi_r, taxi_c = destinations[person_num]
            del destinations[person_num]
            queue = collections.deque()
            queue.append((taxi_r, taxi_c))
            visited = [[False for _ in range(N)] for _ in range(N)]
            visited[taxi_r][taxi_c] = True
            cand = []

        if not queue:
            fuel = -1
            break


N, M, fuel = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]
taxi_r, taxi_c = map(int, input().split())
taxi_r -= 1
taxi_c -= 1
destinations = dict()
for person_num in range(2, M + 2):
    start_r, start_c, arrive_r, arrive_c = map(int, input().split())
    ground[start_r - 1][start_c - 1] = person_num
    destinations[person_num] = (arrive_r - 1, arrive_c - 1)

move(taxi_r, taxi_c)

print(fuel)