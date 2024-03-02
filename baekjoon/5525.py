N = int(input())
M = int(input())
S = input()

start, cnt, res = 0, 0, 0

while start <= M:
  if S[start:start+3] == "IOI":
    cnt += 1
    start += 2
    if cnt == N :
      res += 1
      cnt -= 1
  else :
    start += 1
    cnt = 0

print(res)