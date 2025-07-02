word = input().upper()  # 대소문자 구분 제거

word_list = list(set(word)) # 중복 제거
cnt_list = []

for w in word_list:
  cnt_list.append(word.count(w))

max_cnt = max(cnt_list)
if cnt_list.count(max_cnt) > 1:
  print("?")
else :
  print(word_list[cnt_list.index(max_cnt)])