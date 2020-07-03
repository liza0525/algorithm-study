import sys
sys.stdin = open('../input.txt', 'r')

def find_num(num):
    first, last = 0, N-1
    while True:
        if first > last:
            return 0
        mid = (first + last) // 2
        if nums[mid] == num:
            return 1
        elif nums[mid] > num:
            last = mid - 1
        elif nums[mid] < num:
            first = mid + 1


N = int(input())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
M = int(input())
cands = list(map(int, sys.stdin.readline().split()))
for cand in cands:
    print(find_num(cand))