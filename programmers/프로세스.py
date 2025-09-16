from collections import deque

def solution(priorities, location):
    res = []
    queue = deque()
    for idx, val in enumerate(priorities):
        queue.append((idx, val))
    max_prior = queue[0][1]
    while queue:
        idx, val = queue.popleft()  # 현재
        isMax = True
        for i, v in queue:  # 나머지
            if val < v: # 하나라도 더 큰 게 있으면
                queue.append((idx, val))
                isMax = False
                break
        if isMax:   # 이게 가장 클 때
            res.append((idx, val))
            if idx == location:
                return len(res)