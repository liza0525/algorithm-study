import sys
sys.stdin = open('../input.txt', 'r')

N = int(input())

# A : 각 시험장에 배치되는 응시자 수
A = list(map(int, input().split()))

# B : 총감독이 감독 가능한 인원 수
# C : 부감독이 감독 가능한 인원 수
B, C = map(int, input().split())

total_supervisor = 0

for i in range(N):
    if A[i] > B:
        if (A[i] - B) % C:
            total_supervisor += ((A[i] - B) // C + 1)
        else:
            total_supervisor += (A[i] - B) // C
    total_supervisor += 1

print(total_supervisor)