import sys
sys.stdin = open('../input.txt', 'r')


def find_depth(node):
    global game_play_cnt
    stack = [node]
    level = [0 for _ in range(N+1)]
    while stack:
        now_node = stack.pop()
        is_leaf = True
        for next_node in range(node, N+1):
            if not graph[now_node][next_node]: continue
            if next_node == node: continue
            if level[next_node]: continue
            level[next_node] = level[now_node] + 1
            stack.append(next_node)
            is_leaf = False
        if is_leaf:
            game_play_cnt += level[now_node]


N = int(input())
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(N-1):
    first_node, second_node = map(int, input().split())
    graph[first_node][second_node], graph[second_node][first_node] = 1, 1


game_play_cnt = 0

find_depth(1)

print('Yes' if game_play_cnt % 2 else 'No')