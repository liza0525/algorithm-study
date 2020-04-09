import sys
sys.stdin = open('../input.txt', 'r')

V, E = map(int, input().split())
K = int(input())
info = [list(map(int, input().split())) for _ in range(E)]