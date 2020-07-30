from collections import deque

def solution(bridge_length, weight, trucks):
    time = 0
    trucks = deque(trucks)
    bridge = deque([0] * bridge_length)

    while trucks:
        if trucks:
            bridge.popleft()
            if sum(bridge) + trucks[0] > weight:
                bridge.append(0)
            else:
                bridge.append(trucks.popleft())
        time += 1

    return time + bridge_length


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))