import sys
input = sys.stdin.readline

N = int(input())
col = [0] * N
cnt = 0

# i = 놓은 말 개수
# col[i] = i번째 row 말의 col 좌표
def BackTracking(i):
  global cnt
  if i == N:
    cnt+=1
    return
  else:
    for j in range(N):
      col[i] = j
      if Promising(i):
        BackTracking(i+1)


def Promising(i):
  for k in range(i):
    if col[i] == col[k] or abs(col[i]-col[k]) == abs(i-k):
      return False
  return True

BackTracking(0)
print(cnt)