from collections import deque

class Truck():
    weight = 0
    position = 0
    def __init__(self, weight, position):
        self.weight = weight
        self.position = position


def solution(bridge_length, weight, truck_weights):
    time = 0
    before_bridge = deque()
    on_bridge = deque()

    for truck_weight in truck_weights:
        before_bridge.append(Truck(truck_weight, 1))

    while before_bridge or on_bridge:
        total_weight = 0
        for truck in on_bridge:
            total_weight += truck.weight
            truck.position += 1

        if on_bridge and on_bridge[0].position > bridge_length:
            total_weight -= on_bridge.popleft().weight

        if before_bridge and total_weight + before_bridge[0].weight <= weight and len(on_bridge) <= bridge_length:
            on_bridge.append(before_bridge.popleft())

        time += 1
    return time


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))