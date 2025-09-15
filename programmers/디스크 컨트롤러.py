# 작업의 소요시간이 짧은 것, 작업의 요청 시각이 빠른 것, 작업의 번호가 작은 것 순
import heapq

def solution(jobs):
    jobs.sort()
    
    now_time = 0
    res = []
    heap = []
    n = len(jobs) # 이 부분 인터넷 검색함 (3줄 아래)
    
    # 모든 작업 완료될 때까지
    # while len(res) <= len(jobs): # len(jobs)로 비교하면 job에서 pop을 하니까 크기가 바뀌는 문제 생김
    while len(res) < n:
        # 1. 스케줄링
        # 1-1. 현재 시각까지의 요청 다 넣기
        while jobs and jobs[0][0] <= now_time:
            a = jobs.pop(0)
            # 큐에 a 넣기 (소요시간, 요청 시각 순)
            heapq.heappush(heap, (a[1], a[0]))
        
        # 1-2. 현재 시각까지 요청은 없지만, 아직 요청 남았을 때
        if not heap and jobs:
            # 가장 가까운 요청 넣기
            a = jobs.pop(0)
            # 시간 업데이트 (요청 시각으로)
            now_time = a[0]
            # 큐에 a 넣기
            heapq.heappush(heap, (a[1], a[0]))
            
            
        # 2. 우선 순위대로 큐에서 빼서 작업
        # 큐에서 빼기 (작업 진행)
        work_time, req_time = heapq.heappop(heap)
        # 시간 업데이트 (작업 진행 시간만큼)
        now_time += work_time
        res.append(now_time - req_time)
    
    return sum(res)//n