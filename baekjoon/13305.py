N = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))

res = 0
min_price = price[0]

for i in range(N-1):
  if min_price > price[i]:
    min_price = price[i]
  res += dist[i] * min_price

print(res)