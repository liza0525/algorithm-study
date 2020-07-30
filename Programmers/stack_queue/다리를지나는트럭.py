from collections import deque

def solution(bridge_length, weight, trucks):
    time = 0
    trucks = deque(trucks)
    truck_num = len(trucks)
    passed, bridge = deque(), deque()
    while len(passed) < truck_num:
        if not bridge:
            bridge.append(trucks.popleft())
            time += 1
        if len(bridge) == bridge_length:
            passed.append(bridge.popleft())
            bridge.append(trucks.popleft())
            time += (bridge_length + 1)
        else:
            if sum(bridge) + trucks[0] > weight:
                pass
            else:
                pass


    return time


print(solution(2, 10, [7, 4, 5, 6]))