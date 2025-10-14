# 풀이1 : dfs (시간 초과)
def solution(m, n, puddles):
    res = 0
    min_dist = float('inf')
    puddles_set = {(x-1, y-1) for x, y in puddles}
    
    def dfs(x, y, dist):
        nonlocal min_dist
        nonlocal res
        
        if not (0 <= x < m and 0 <= y < n) or (x, y) in puddles_set:
            return
        
        if (x, y) == (m-1, n-1):
            # 최단 거리일 때 -> 해당 거리를 최단 거리로 초기화
            if dist < min_dist:
                min_dist = dist
                res = 1
            # 최단 거리와 같을 때 -> res += 1
            elif dist == min_dist:
                res += 1
            return
        
        dfs(x+1, y, dist+1)
        dfs(x, y+1, dist+1)
        
    dfs(0, 0, 0)
    return res

# 풀이2 : dp
# 어차피 오, 아래로만 이동하면 무조건 최단 경로
# 즉, 해당 지점 몇 번 거치는지만 계산하면 됨
def solution(m, n, puddles):
    dp = [[0]*n for _ in range(m)]
    
    for x, y in puddles:
        dp[x-1][y-1] = -1
        
    dp[0][0] = 1
    
    for i in range(m):
        for j in range(n):
            if dp[i][j] == -1:
                dp[i][j] = 0 # 안바꾸면 다른 곳에서 -1 더해짐
                continue
            if i > 0:
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]
                
    return dp[m-1][n-1] % (1000000007)
                