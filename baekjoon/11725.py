import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

visited = [0 for _ in range(N+1)] # 해당 인덱스의 부모 노드 저장
def DFS(n): # n이 부모
  for i in graph[n]:  
    if visited[i] == 0: 
      visited[i] = n
      DFS(i)
DFS(1)

for i in range(2, len(visited)):
  print(visited[i])