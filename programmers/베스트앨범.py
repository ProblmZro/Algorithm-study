# 장르 > 노래 > 고유 번호
def solution(genres, plays):
    arr = {}
    for i in range(len(genres)):
        if genres[i] not in arr:
            arr[genres[i]] = [(plays[i], i)]
        else:
            arr[genres[i]].append((plays[i], i))
    
    # arr = {'classic': [(500, 0), (150, 2), (800, 3)], 'pop': [(600, 1), (2500, 4)]}

    # 1. 장르 순 정렬
    arr = sorted(arr.items(), 
                 key=lambda x:sum(play for play, idx in x[1]), 
                 reverse=True)
    
    # 2. 노래, 고유번호 순 정렬
    new_arr = {}
    for key, value in arr:
        new_arr[key] = sorted(value, key=lambda x: (-x[0], x[1]))

    # new_arr = {'pop': [(2500, 4), (600, 1)], 'classic': [(800, 3), (500, 0), (150, 2)]}
    res = []
    for song_list in new_arr.items():
        cnt = 0
        for play, idx in song_list[1]:
            res.append(idx)
            cnt += 1
            if cnt == 2:
                break
    
    return res