import sys
sys.stdin = open('../input.txt', 'r')

N = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)

new_average = sum(scores) / max_score * 100 / N
print(new_average)
