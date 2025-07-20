from collections import deque

N, K = map(int, input().split())
visited = [-1] * 100001  # -1은 방문 안 한 것

def bfs(v):
    queue = deque([v])
    visited[v] = 0  # 시작점 거리 0

    while queue:
        cur = queue.popleft()
        if cur == K:
            print(visited[cur])
            return
        for i in (cur*2, cur+1, cur-1):  # 순서는 상관없음!
            if 0 <= i <= 100000 and visited[i] == -1:
                visited[i] = visited[cur] + 1
                queue.append(i)

bfs(N)

# 0 1 -> 2 예외