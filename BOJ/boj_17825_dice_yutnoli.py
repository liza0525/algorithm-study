import sys
sys.stdin = open('../input.txt', 'r')

def play(score, depth):
    global max_score
    if depth == 10:
        max_score = max(max_score, score)
    else:
        for num in range(4):
            road, idx = locations[num]
            if road == 4 and idx == 4: continue

            dice = dices[depth]
            next_road, next_idx = road, idx + dice

            if next_road == 0:
                if next_idx == 5:
                    next_road, next_idx = 1, 0
                elif next_idx == 10:
                    next_road, next_idx = 2, 0
                elif next_idx == 15:
                    next_road, next_idx = 3, 0
                elif next_idx == 20:
                    next_road, next_idx = 4, 3
                elif next_idx >= 21:
                    next_road, next_idx = 4, 4
            elif next_road == 4:
                if next_idx > len(infos[next_road]) - 1:
                    next_idx = len(infos[next_road]) - 1
            else:
                if next_idx >= len(infos[next_road]):
                    next_road, next_idx = 4, next_idx - len(infos[next_road])

            if not (next_road == 4 and next_idx == 4):
                if [next_road, next_idx] in locations:
                    continue

            locations[num] = [next_road, next_idx]
            play(score + infos[next_road][next_idx], depth + 1)
            locations[num] = [road, idx]


dices = list(map(int, input().split()))
max_score = 0

# 윷놀이 판 설명
infos = [[score for score in range(0, 40, 2)],
         [10, 13, 16, 19],
         [20, 22, 24],
         [30, 28, 27, 26],
         [25, 30, 35, 40, 0]]

locations = [[0, 0] for _ in range(4)] # 말이 놓여진 곳의 길 번호, 인덱스

play(0, 0)

print(max_score)