import sys
sys.stdin = open('contact.txt','r')
from pprint import pprint

for test in range(10):
    n, s = map(int,input().split())
    inputdata = list(map(int, input().split()))
    infos = [[inputdata[i], inputdata[i+1]] for i in range(0, len(inputdata), 2)]
    cnt = 0
    print(infos)