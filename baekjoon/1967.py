import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def DFS(n, w):
  for i in graph[n]:
    node, weight = i
    if dist[node] == -1:
      dist[node] = weight + w
      DFS(node, dist[node])

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
  p, c, w = map(int, input().split())
  graph[p].append([c, w])
  graph[c].append([p, w])

dist = [-1 for _ in range(N+1)]
dist[1] = 0
DFS(1, 0)

far = dist.index(max(dist))

dist = [-1 for _ in range(N+1)]
dist[far] = 0
DFS(far, 0)

print(max(dist))