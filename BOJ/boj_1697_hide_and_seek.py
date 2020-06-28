import sys
sys.stdin = open('../input.txt', 'r')


def seeking(num):
    stack = []
    visited = [0] * 10001
    stack.append(num)
    visited[num] = 1
    cnt = 0

    while stack:
        temp = stack[:]
        stack = []
        while temp:
            s = temp.pop(0)
            if 0 <= s-1 <= 10000 and not visited[s-1]:
                stack.append(s-1)
                visited[s-1] = 1
            if 0 <= s+1 <= 10000 and not visited[s+1]:
                stack.append(s+1)
                visited[s+1] = 1
            if 0 <= s*2 <= 10000 and not visited[s*2]:
                stack.append(s*2)
                visited[s*2] = 1
        cnt += 1
        if visited[K] == 1:
            return cnt


N, K = map(int, sys.stdin.readline().split())
print(seeking(N))
