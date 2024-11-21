import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N, R, Q = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

cnt = [0] * (N+1)
def countVertex(n):
  cnt[n] = 1
  for i in graph[n]:
    if cnt[i] == 0:
      countVertex(i)
      cnt[n] += cnt[i]

countVertex(R)
for _ in range(Q):
  print((cnt[int(input())]))