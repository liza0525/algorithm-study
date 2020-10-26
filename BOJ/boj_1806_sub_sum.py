import sys
sys.stdin = open('../input.txt', 'r')

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

sub_sums = [0 for _ in range(N+1)]
# sub_sums[0] = numbers[0]

for idx in range(1, N+1):
    sub_sums[idx] = sub_sums[idx-1] + numbers[idx-1]

# print(sub_sums)

min_length = 100001
start, end = 0, 0

while start != N:
    sub_sum = sub_sums[end] - sub_sums[start]

    if sub_sum >= S:
        min_length = min(min_length, end - start)
        start += 1
    elif sub_sum < S:
        if end != N:
            end += 1
        else:
            start += 1

print(min_length if min_length != 100001 else 0)