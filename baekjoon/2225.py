import sys
input = sys.stdin.readline

def DFS():
  global ans
  if len(arr) == K:
    if sum(arr) == N:
      ans += 1
    return
  for i in range(0, N+1):
    arr.append(i)
    DFS()
    arr.pop()

N, K = map(int, input().split())
arr = []
ans = 0
DFS()
print(ans % 1000000000)