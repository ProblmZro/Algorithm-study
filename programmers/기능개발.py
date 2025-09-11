def solution(progresses, speeds):
    day = []
    for progress, speed in zip(progresses, speeds):
        day_temp = (100-progress) // speed
        if (100-progress) % speed != 0:
            day_temp += 1
        day.append(day_temp)
    
    res = []
    a = day.pop(0)
    num = 1
    while len(day) > 0:
        b = day.pop(0)
        if a >= b:  # 다음 기능이 덜 걸릴 때
            num += 1
        else : # 다음 기능이 더 오래 걸릴 때
            res.append(num)
            a = b
            num = 1   
    
    res.append(num) # 남아있는 num 넣기
    
    return res


# [7, 3, 9]
# [5, 10, 1, 1, 20, 1]
