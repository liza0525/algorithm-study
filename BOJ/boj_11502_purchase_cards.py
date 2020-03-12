N = int(input())
p = list(map(int, input().split()))
p.insert(0, 0)
mp = [0] * (N+1)
mp[1] = p[1]
for i in range(2, N+1):
    for j in range(1, i+1):
        mp[i] = max(mp[i], mp[i-j]+p[j])

print(mp[N])