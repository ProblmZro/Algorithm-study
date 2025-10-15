# 동전을 하나씩 넣으며 dp[i]의 경우 i를 만드는 경우의 수 계산
# 예시 : i=4이고, 동전 2 넣을 때
# dp[4] = dp[4] + dp[4-2]
# 1로 4 만드는 경우 (dp[4]) + 2 만든 거에 2 넣는 경우의 수 (dp[4-2])

n, k = map(int, input().split())
coins = []
for _ in range(n):
  coins.append(int(input()))

dp = [0] * (k+1)
dp[0] = 1

for coin in coins:
  for i in range(coin, k+1):
    dp[i] += dp[i-coin]

print(dp[-1])