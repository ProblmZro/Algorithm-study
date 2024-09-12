N, M = map(int, input().split())
S, tmp = [], []

for _ in range(N):
  S.append(input())
S.sort()

for _ in range(M):
  tmp.append(input())
tmp.sort()

cnt = 0
i, j = 0, 0
while j < M and i < N:
  if S[i][0:len(tmp[j])] == tmp[j]:
    cnt += 1
    j += 1
    continue
  elif S[i] > tmp[j]:
    j += 1
    continue
  elif S[i] < tmp[j]:
    i += 1
    continue
      
print(cnt)