import sys
sys.stdin = open('../input.txt', 'r')
from pprint import pprint

def is_field(r, c):
    return 0 <= r < N and 0 <= c < N

def set_bridge(ground):
    isBridge = [[False for _ in range(N)] for _ in range(N)]
    bridge_num = 0

    for r in range(N):
        toggle = False
        for c in range(N-1):
            now_height, next_height = ground[r][c], ground[r][c+1]
            if now_height == next_height: # 단차가 없는 경우
                continue

            elif now_height - 1 == next_height: # 내려가는 단차인 경우
                for l in range(1, L+1):
                    if not is_field(r, c+l): # 범위 밖이면 다리 못 놓음
                        toggle = True
                        break
                    if ground[r][c+l] != next_height: # 다리 놓을 땐 단차가 없어야 함
                        toggle = True
                        break
                else: # 단차 없음 확인 -> 다리 놓기
                    isBridge[r][c+1:c+1+L] = [True] * L

                if toggle:
                    break

            elif now_height + 1 == next_height: # 올라가는 단차인 경우
                for l in range(L): # 이 때는 현재위치부터 지나온 길들을 확인하며 다리 놓을 여부 확인
                    if not is_field(r, c-l): # 범위 밖이면 다리 못 놓음
                        toggle = True
                        break
                    if ground[r][c-l] != now_height: # 다리 놓을 때 단차가 없어야 함
                        toggle = True
                        break
                    if isBridge[r][c-l]: # 다리가 이미 놓여져 있는 경우
                        toggle = True
                        break
                else:
                    isBridge[r][c+1-L:c+1] = [True] * L

                if toggle:
                    break

            else: # 단차가 2 이상인 경우
                break

        else: # 길이 연결된 경우
            bridge_num += 1

    return bridge_num


N, L = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]
total_bridge = 0
total_bridge += set_bridge(ground)
total_bridge += set_bridge(list(map(list, zip(*ground))))

print(total_bridge)