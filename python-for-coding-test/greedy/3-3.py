n, m = map(int, input().split())
lst = []
for _ in range(n):
  lst.append(list(map(int, input().split())))
  min_val = min(lst)
  res = max(res, min_val)
print(res)