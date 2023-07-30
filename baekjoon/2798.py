from itertools import combinations

n, m = map(int, input().split())
card = list(map(int, input().split()))
res = 0

for i in combinations(card, 3) :
  if sum(i) <= m:
    res = max(res, sum(i))

print(res)