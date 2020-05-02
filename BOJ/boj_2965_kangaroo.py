import sys
sys.stdin = open('../input.txt', 'r')


lk, mk, rk = map(int, input().split())
print(mk - lk - 1) if mk - lk > rk - mk else print(rk - mk - 1)