import sys
sys.stdin = open('inputdata/boj_9095_add123.txt', 'r')

def dp(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    else:
        return dp(num-1)+dp(num-2)+dp(num-3)

for test in range(int(input())):
    n = int(input())
    print('#{} {}'.format(test+1, dp(n)))