N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
home = []
store = []

for i in range(N):
  for j in range(N):
    if city[i][j] == 1:
      home.append((i, j))
    elif city[i][j] == 2:
      store.append((i, j))

store_idx = []
ans = 10e9

def backTracking(idx):
  global ans
  if len(store_idx) == M:
    res = 0
    for h in home:
      dist = 10e9
      for s in store_idx:
        dist = min(abs(s[0]-h[0]) + abs(s[1]-h[1]), dist)
      res += dist
    ans = min(ans, res)
    return 
  
  for i in range(idx, len(store)):
    store_idx.append(store[i])
    backTracking(i+1)
    store_idx.pop()

backTracking(0)
print(ans)