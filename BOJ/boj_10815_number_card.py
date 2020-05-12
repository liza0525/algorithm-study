import sys
sys.stdin = open('../input.txt', 'r')

N = int(input())
answer = list(map(int, input().split()))
M = int(input())
predict = list(map(int, input().split()))
p = dict()
for pn in predict:
    p.update({pn: 0})

for a in answer:
    if a in p.keys():
        p[a] = 1

print(' '.join(map(str, p.values())))