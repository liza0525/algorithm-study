import sys
sys.stdin = open('../input.txt', 'r')

T = int(input())

for _ in range(T):
    N = int(input())
    zero = [1, 0]
    one = [0, 1]

    for i in range(2, N+1):
        cnt_zero = zero[i-1] + zero[i-2]
        zero.append(cnt_zero)
        cnt_one = one[i-1] + one[i-2]
        one.append(cnt_one)

    print(zero[N], one[N])