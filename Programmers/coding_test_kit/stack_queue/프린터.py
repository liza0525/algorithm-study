# 백준 1966 프린터큐와 동일 문제
from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque()
    for i, priority in enumerate(priorities):
        queue.append([priority, i])

    while True:
        if queue[0][0] == max(queue)[0]:
            prior, num = queue.popleft()
            answer += 1
            if num == location:
                return answer
        else:
            queue.append(queue.popleft())