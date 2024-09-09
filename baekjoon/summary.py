# --------------
# dfs : 모든 노드 방문, 그래프 탐색의 일반적인 경우
# --------------
def dfs(graph, v, visited):
  # 현재 노드 방문 처리
  visited[v] = True
  print(v, end=' ')

  # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)



# --------------
# bfs : 두 노드간 최단 경로, 임의의 경로 탐색
# --------------
from collections import deque

def bfs(graph, start, visited):
  queue = deque([start])
  # node visited
  visited[start] = True

  # loop till queue is empty
  while queue:
    # visted node 'v' 
    v = queue.popleft()
    print(v, end=' ')

    # v 노드에 연결된 노드들 투입 -> 방문 안한 노드만 queue에 추가
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        # print(queue) # queue안에 뭐있나
        visited[i] = True


# --------------
# quick sort
# --------------
array = [2, 3, 1, 4]
def quick_sort(array):
  #quit if list has one or less elements
  if len(array) <= 1:
    return array
  
  pivot = array[0] # first element as pivot
  tail = array[1:] # list accept pivot
  left = [x for x in tail if x <= pivot] # left side
  right = [x for x in tail if x > pivot] # right side
  return quick_sort(left) + [pivot] + quick_sort(right)


# --------------
# 이진 탐색 (배열 데이터가 정렬되어 있어야 함)
# --------------
def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid -1
    else:
      start = mid +1
  return None
result = binary_search(array, target, 0, n - 1)


# --------------
# DP (Top-down)
# --------------
# Memoization 초기화
d = [0] * 100

def fibo(x):
  # base case
  if x == 1 or x == 2:
    return 1
  if d[x] != 0:
    return d[x]
  # 점화식을 그대로 구현
  d[x] = fibo(x-1) + fibo(x-2)
  return d[x]


# --------------
# DP (Bottom-up)
# --------------
# initiate DP Table
d = [0] * 100
# both first Fibonacci number and second fibonacci number are 1
d[1] = 1
d[2] = 1
n = 99
# bottom up dynamic programming
for i in range(3, n+1):
    d[i] = d[i - 1] + d[i - 2]