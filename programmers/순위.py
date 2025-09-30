# 방법 1 : bfs
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

# 방법 2 : 플로이드-워셜
# 자신 노드 기준으로 이기는 노드 + 지는 노드 구함

def solution(n, results):
    board = [[0] * (n+1) for _ in range(n+1)]
    
    for a, b in results:
        board[a][b] = 1     # 이기면 1
        board[b][a] = -1    # 지면 -1
        
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                if board[a][b] == 0:    # 아직 결정 안됐으면
                    # a -> k -> b 이기면 a -> b 이김
                    if board[a][k] == 1 and board[k][b] == 1:
                        board[a][b] = 1
                    # a -> k -> b 지면 a -> b 짐
                    if board[a][k] == -1 and board[k][b] == -1:
                        board[a][b] = -1
                    
    # 결정되지 않은 (0) 개수가 2개 (자기 자신, 인덱스 0)이면 결정됨
    res = 0
    for bs in board:
        cnt = 0
        for b in bs:
            if b == 0:
                cnt += 1
        if cnt == 2:
            res += 1
            
    return res
	            