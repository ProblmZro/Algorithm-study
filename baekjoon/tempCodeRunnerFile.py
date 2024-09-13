N, M = map(int, input().split())
S = []

for _ in range(N):
  S.append(input())

cnt = 0
for _ in range(M):
  tmp = input()
  for i in S:
    if i[0] == tmp[0]:
      cnt += 1
      break

print(cnt)