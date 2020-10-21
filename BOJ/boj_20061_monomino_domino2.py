import sys
sys.stdin = open('../input.txt', 'r')
from pprint import pprint

def play(block_shape, c, block_num, ground):
    global res_score
    r = 0
    # 블록 내리기
    while True:
        if block_shape == 2:
            if r == 5 or ground[r+1][c] or ground[r+1][c+1]: break
            else: r += 1
        else:
            if r == 5 or ground[r+1][c]:
                break
            else: r += 1

    ground[r][c] = block_num
    if block_shape == 2:
        ground[r][c+1] = block_num
    elif block_shape == 3:
        ground[r-1][c] = block_num

    # 줄 없애기
    line_idxs = []
    line_cnt = 0
    for line in range(6):
        for idx in range(4):
            if ground[line][idx] == 0:
                break
        else:
            res_score += 1
            line_cnt += 1
            line_idxs.append(line)
            

    # 줄 없어졌을 때 블록 내리기
    if line_idxs:
        for line_idx in list(reversed(line_idxs)):
            ground.pop(line_idx)

        for _ in range(line_cnt):
            ground.insert(0, [0 for _ in range(4)])

    # 0, 1행 확인
    while True:
        if sum(ground[1]) != 0:
            ground.pop()
            ground.insert(0, [0 for _ in range(4)])
        else:
            break


N = int(input())
infos = [list(map(int, input().split())) for _ in range(N)]
res_score = 0
green_g = [[0 for _ in range(4)] for _ in range(6)]
blue_g = [[0 for _ in range(4)] for _ in range(6)]

block_num = 1
for block_shape, r, c in infos:
    play(block_shape, c, block_num, green_g)

    if block_shape == 1:
        play(block_shape, 3-r, block_num, blue_g)
    elif block_shape == 2:
        play(3, 3-r, block_num, blue_g)
    elif block_shape == 3:
        play(2, 3-r-1, block_num, blue_g)

    block_num += 1

remain_block = 0
for r in range(6):
    for c in range(4):
        if green_g[r][c]:
            remain_block += 1
        if blue_g[r][c]:
            remain_block += 1

print(res_score)
print(remain_block)