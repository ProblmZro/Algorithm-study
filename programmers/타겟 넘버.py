# 방법1 (DFS)
res = 0
def dfs(sum_num, idx, numbers, target):
    global res
    if idx == len(numbers):
        if target == sum_num:
            res += 1
        return 
    
    dfs(sum_num+numbers[idx], idx+1, numbers, target)
    dfs(sum_num-numbers[idx], idx+1, numbers, target)

def solution(numbers, target):
    dfs(0, 0, numbers, target)
    return res
        
# 방법2 (BFS)
from collections import deque

def solution(numbers, target):
    res = 0
    queue = deque()
    # 시작은 idx=0, sum=0
    queue.append((0, 0))
    
    while queue:
        idx, num = queue.popleft()
        
        if idx < len(numbers):
            queue.append((idx+1, num+numbers[idx]))
            queue.append((idx+1, num-numbers[idx]))
        else:
            if num == target:
                res += 1
                
    return res