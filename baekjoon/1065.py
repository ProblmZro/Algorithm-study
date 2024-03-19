N = int(input())
cnt = 0

if N >= 100:
  for i in range(100, N+1): 
    lst = []
    while i > 0:
      lst.append(i % 10)
      i //= 10
    if lst[0] - lst[1] == lst[1] - lst[2]:
      cnt += 1
  cnt += 99
else :
  cnt = N

if N == 1000:
  cnt -= 1

print(cnt)