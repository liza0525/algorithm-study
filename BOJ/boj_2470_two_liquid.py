import sys
sys.stdin = open('../input.txt', 'r')

def solve(liquids):
    min_sum = 10e10
    min_ans, max_ans = 0, 0

    left, right = 0, N-1

    while left < right:
        cand_sum = liquids[left] + liquids[right]
        if cand_sum == 0:
            return liquids[left], liquids[right]

        if abs(cand_sum) < min_sum:
            min_sum = abs(cand_sum)
            min_ans, max_ans = liquids[left], liquids[right]

        if cand_sum > 0:
            right -= 1
        else:
            left += 1

    return min_ans, max_ans


N = int(sys.stdin.readline())
min_ans, max_ans = 0, 0

liquids = sorted(list(map(int, sys.stdin.readline().split())))

if liquids[0] > 0:
    min_ans, max_ans = liquids[0], liquids[1]
elif liquids[N-1] < 0:
    min_ans, max_ans = liquids[N-2], liquids[N-1]
else:
    min_ans, max_ans = solve(liquids)

print(min_ans, max_ans)