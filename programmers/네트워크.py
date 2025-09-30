def solution(n, computers):
    res = 0
    visited = [False] * n
    for next_com in range(n):
        if visited[next_com] == False:
            dfs(next_com, visited, n, computers)
            res += 1 
    return res

def dfs(now, visited, n, computers):
    visited[now] = True
    
    for next_com in range(n):
        # 나 자신이 아니고 연결된 애
        if next_com != now and computers[now][next_com] == 1:
            if not visited[next_com]:
                dfs(next_com, visited, n, computers)