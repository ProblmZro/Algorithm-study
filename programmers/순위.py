# 선수마다 해당 선수를 bfs 탐색으로 이긴 사람 + 진 사람 탐색
from collections import deque

def solution(n, results):
    win = [[] for _ in range(n+1)]
    lose = [[] for _ in range(n+1)]
    
    for a, b in results:
        win[a].append(b)
        lose[b].append(a)

    def bfs(start, graph):
        visited = [False] * (n+1)
        cnt = 0 # 몇 명이 나를 이겼는지 or 졌는지
        
        queue = deque()
        queue.append(start)
        visited[start] = True
        
        while queue:
            now = queue.popleft()
            for next in graph[now]:
                if not visited[next]:
                    queue.append(next)
                    visited[next] = True
                    cnt += 1
        
        return cnt
    
    res = 0
    for i in range(1, n+1):
        win_cnt = bfs(i, win)
        lose_cnt = bfs(i, lose)
        if win_cnt + lose_cnt == n-1:
            res += 1
        
    return res