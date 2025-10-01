# t분 동안 받을 수 있는 사람 수 계산 (즉, 답을 기준으로 탐색)
def solution(n, times):
    times.sort()
    
    start = 1
    end = times[-1] * n # 최악의 경우 (max)
    res = end
    
    while start <= end:
        mid = (start + end) // 2
        cnt = 0 # 입국심사 완료한 사람 수
        
        for time in times:
            cnt += mid // time # mid분 동안 받을 수 있는 사람
        
        if cnt < n: # 시간 더 필요 (입국심사 덜 함)
            start = mid + 1
            
        else:   # 1. 시간 넘쳐남 (더 많은 사람 입국심사)
                # 2. 정답이지만, 더 적게 하고도 다 완료할 가능성 존재
            res = mid
            end = mid - 1
            
    return res
    
