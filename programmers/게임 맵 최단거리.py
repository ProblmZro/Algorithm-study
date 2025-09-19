from collections import deque

def solution(maps):
    
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    
    queue = deque()
    queue.append((0,0))
    visited[0][0] = 1
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if 0<=nx<len(maps) and 0<=ny<len(maps[0]) and maps[nx][ny]==1 and visited[nx][ny]==0:
                queue.append((nx,ny))
                visited[nx][ny] = visited[x][y] + 1
    
    res = visited[len(maps)-1][len(maps[0])-1]
    if visited[len(maps)-1][len(maps[0])-1] == 0:
        return -1
    
    return visited[len(maps)-1][len(maps[0])-1]