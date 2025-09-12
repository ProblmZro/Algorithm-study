# 계속해서 작은 값 뽑아야 함 (sort 비효율) -> 힙
# 힙 문법 기억 안나서 찾아봄
import heapq

def solution(scoville, K):
    heapq.heapify(scoville)  # 존재하는 리스트를 힙에 넣기
    cnt = 0
    
    while True:
        if scoville[0] >= K:
            return cnt
        if len(scoville) < 2:
            return -1
        
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        new = a + b*2
        cnt += 1
        heapq.heappush(scoville, new)