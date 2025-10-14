from collections import deque

# 테두리 1, 내부 0, 외부 -1
# 붙어있는 경우 문제 발생 -> 다 두배씩 늘리고 마지막에 2로 나누기
def solution(rectangle, characterX, characterY, itemX, itemY):
    res = 0
    graph = [[-1] * 102 for _ in range(102)]
    visited = [[1] * 102 for _ in range(102)]
    direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    
    for rect in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, rect)
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if x1 < i < x2 and y1 < j < y2: # 내부
                    graph[i][j] = 0
                elif graph[i][j] != 0:  # 테두리 (내부 표시한 거 빼고)
                    graph[i][j] = 1
    
    cx, cy, ix, iy = characterX*2, characterY*2, itemX*2, itemY*2
    
    queue = deque()
    queue.append((cx, cy))
    
    while queue:
        x, y = queue.popleft()
        
        if x == ix and y == iy:
            res = visited[x][y] // 2
            break
        
        for i in range(4):
            dx, dy = x + direction[i][0], y + direction[i][1]
            if 0 <= dx < 102 and 0 <= dy < 102:
                if graph[dx][dy] == 1 and visited[dx][dy] == 1:
                    visited[dx][dy] += visited[x][y]
                    queue.append((dx, dy))
                    
    return res