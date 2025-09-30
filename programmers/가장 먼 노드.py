from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    dist = [0] * (n+1)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    queue = deque()
    queue.append(1)    # 노드
    dist[1] = 1
    
    while queue:
        node = queue.popleft()
        
        for next in graph[node]:
            if dist[next] != 0:
                continue
            queue.append(next)
            dist[next] = dist[node] + 1
            
    longest = max(dist)
    res = 0
    for i in dist:
        if max(dist) == i:
            res += 1
            
    return res
            