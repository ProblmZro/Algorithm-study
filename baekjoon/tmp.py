def solution(m, musicinfos):
    result = []
    i = 0
    for music in musicinfos:
        info = list(music.split(","))
        start_time_list = info[0].split(":")
        stop_time_list = info[1].split(":")
        start_time = int(start_time_list[0])*60 + int(start_time_list[1])
        stop_time = int(stop_time_list[0])*60 + int(stop_time_list[1])
        playing_time = stop_time - start_time

        music_list = []
        j = 0
        for i in range(len(info[3])):
            if info[3][i] == '#':
                music_list[j-1] += '#'
                continue
            music_list.append(info[3][i])
            j+=1

        tmp = []
        music_len = len(music_list)
        if playing_time <= music_len:
            tmp = music_list[:playing_time]
        else:
            quotient = playing_time // music_len
            remainder = playing_time % music_len
            if remainder:
                tmp = music_list * quotient + music_list[:remainder-1]
            else:
                tmp = music_list * quotient
        real_playing_music = "".join(tmp)
        if m in real_playing_music:
            result.append([playing_time, i, info])
        i+=1
    if len(result) == 0:
        return "(None)"
    result = sorted(result, key=lambda x:(-x[0], x[1]))
    answer = result[0][2][2]
    print(result)
    return answer

print(solution("ABC",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))