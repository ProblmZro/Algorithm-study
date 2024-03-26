N, K = map(int, input().split())
coins = []
for _ in range(N) :
  coins.append(int(input()))

cnt = 0
for coin in reversed(coins):
  cnt += (K // coin)
  K %= coin

print(cnt)