'''
트리의 지름 구하는 법
  1. 임의의 점(A)에서 가장 먼 지점 B를 찾음
  2. B에서 가장 먼 지점(C)를 찾음
  3. B~C의 거리가 트리의 지름
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

V = int(input())
tree = [[] for _ in range(V+1)]
visited = [0] * (V+1)

for _ in range(V):
  input_list = list(map(int, input().split()))
  x = input_list[0]

  idx = 1
  while input_list[idx] != -1:
    tree[x].append((input_list[idx], input_list[idx+1]))
    idx += 2


def dfs(vertex, dist):
 for v, d in tree[vertex]:
   if visited[v] == 0:
     visited[v] = dist + d
     dfs(v, visited[v])


dfs(1, 0)
visited[1] = 0

tmp_val = 0
far_idx = 1
for i in range(1, V+1):
  if tmp_val < visited[i]:
    tmp_val = visited[i]
    far_idx = i

visited = [0] * (V+1)
dfs(far_idx, 0)
visited[far_idx] = 0
print(max(visited))