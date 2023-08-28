N, K = map(int, input().split())
coin = []
for _ in range(N):
  coin.append(int(input()))

ans = 0
for i in reversed(range(N)):
    ans += (K // coin[i])
    K %= coin[i]

print(ans)