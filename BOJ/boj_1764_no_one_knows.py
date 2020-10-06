# 듣보잡 영어로 뭐라 해야함...?
import sys
sys.stdin = open('../input.txt', 'r')

N, M = map(int, input().split())
people = dict()

for _ in range(N):
    name = input()
    people[name] = 0

for _ in range(M):
    name = input()
    if name in people.keys():
        people[name] = 1

people_num = 0
people = sorted([(k, v) for k, v in people.items()], key=lambda x: x[0])
print(sum(list(zip(*people))[1]))
for k, v in people:
    if v == 1:
        print(k)