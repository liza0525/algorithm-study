import sys
sys.stdin = open('../input.txt', 'r')


for test in range(int(input())):
    N, K = map(int, input().split())
    line = input()
    memo = []
    nums = []
    for i in range(N//4):
        for j in range(0, N, N//4):
            if line[j:j+(N//4)] not in memo:
               memo.append(line[j:j+(N//4)])
        line = line[N-1] + line[:N-1]

    for i in range(len(memo)):
        nums.append(int(memo[i], 16))
    print('#{} {}'.format(test+1, sorted(nums)[len(nums)-K]))
