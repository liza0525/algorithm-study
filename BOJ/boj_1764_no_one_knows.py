# 듣보잡 영어로 뭐라 해야함...?
import sys
sys.stdin = open('../input.txt', 'r')

N, M = map(int, input().split())
deuddo = dict()
bodo = dict()

for _ in range(N):
    name = input()
    deuddo[name] = 1

for _ in range(M):
    name = input()
    bodo[name] = 1

people = sorted(list(set(deuddo.keys()) & set(bodo.keys())))
print(len(people))
for person in people:
    print(person)