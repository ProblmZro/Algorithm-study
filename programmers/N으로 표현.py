# N을 1~8번 사용할 때 나오는 수 리스트 뽑아 저장
# n번 사용 경우의 수 : (n-1번 사용 + 1번 사용) + (n-2번 사용 + 2번 사용) + ...
# 시간 초과 : list -> set (중복 숫자 제거)
def solution(N, number):
    dp = [set() for _ in range(9)]
    
    for i in range(1, 9):   # 8보다 크면 -1
        dp[i].add(int(str(N)*i)) # 5, 55, 555, ...
        
        for j in range(1, i):
            for op1 in dp[j]:
                for op2 in dp[i-j]:
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0:
                        dp[i].add(op1 // op2)
            
        if number in dp[i]:
            return i
    
    else:
        return -1
 
