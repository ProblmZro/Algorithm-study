words = []
for _ in range(int(input())):
  words.append(input())
words.sort(key=len)

cnt = 0
for i in range(len(words)):
  flag = False
  for j in range(i+1, len(words)):
    if words[i] == words[j][:len(words[i])]:
      flag = True
      break
  if not flag:
    cnt += 1

print(cnt)