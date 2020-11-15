import sys
sys.stdin = open('../input.txt', 'r')

N = int(input())

for _ in range(N):
    line = input()
    total_score = 0
    combo_score = 0

    for quiz in line:
        if quiz == 'O':
            combo_score += 1
            total_score += combo_score
        elif quiz == 'X':
            combo_score = 0

    print(total_score)