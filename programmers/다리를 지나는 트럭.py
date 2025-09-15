from collections import deque

def solution(bridge_length, weight, truck_weights):
    onTheBridge = deque()
    passedTheBridge = []
    cnt = 1
    n = len(truck_weights)
    
    while True:
        if not truck_weights and len(passedTheBridge) == n:
            return cnt
        # 다리에 트럭 있을 때 -> 트럭 무게 합 구하기
        tmp_weight = 0
        if onTheBridge:
            for truck in onTheBridge:
                tmp_weight += truck[0]
                truck[1] += 1
                
        # 다음 트럭 넣어도 될 때 -> 트럭 넣기
        if truck_weights and truck_weights[0] + tmp_weight <= weight:
            onTheBridge.append([truck_weights.pop(0), 1])
                    
        if onTheBridge and onTheBridge[0][1] == bridge_length:
            passedTheBridge.append(onTheBridge.popleft())

        cnt += 1
        
        
        