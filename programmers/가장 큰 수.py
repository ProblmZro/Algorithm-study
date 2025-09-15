# 다 같은 자리수로 만들면? (0~1000 -> 세자리로)
# 3 -> 333 / 30 -> 303 / 34 -> 340 / 1000 -> 100
# 342 34 / 344 34 세자리는 이런 거 정렬 애매
# 1~3자리니까 아예 다 6자리로 ㄱㄱ
# 3 -> 333333 / 30 -> 303030 / 343 -> 343343 / 1000 -> 100000

def solution(numbers):
    nums = {}
    for i in range(len(numbers)):
        num = numbers[i]
        if num < 10:
            nums[i] = num*111111
        elif num < 100:
            nums[i] = num*10101
        elif num < 1000:
            nums[i] = num*1001
        else:
            nums[i] = 100000
    sorted_nums = sorted(nums.items(), key=lambda x: x[1], reverse=True)
    # sorted_nums = [(4, 999), (3, 555), (2, 343), (0, 333), (1, 303)]
    res = ""
    for r in sorted_nums:
        res += str(numbers[r[0]])
    
    # [0, 0] -> 00 반례 (답 : 0)
    return str(int(res))