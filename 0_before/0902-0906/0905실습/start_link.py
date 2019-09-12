import sys
import random
sys.stdin = open('start_link.txt', 'r')

n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]
t1 = [i for i in range(n)]
t2 = []