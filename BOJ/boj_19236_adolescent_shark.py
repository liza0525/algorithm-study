from pprint import pprint
import sys
sys.stdin = open('../input.txt', 'r')

ds = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]


def rotate_move(): # 물고기 움직이기
    pass

def eating(i, j, ndi, ndj): # 현재 인덱스와 현재 바라보는 방향
    pass


g = [[[0, 0] for _ in range(4)] for _ in range(4)]
max_res = 0
for i in range(4):
    line = list(map(int, input().split()))
    for j in range(4):
        g[i][j][0], g[i][j][1] = line[2*j], line[2*j+1] # 물고기 번호와 물고기 방향

print(max_res)