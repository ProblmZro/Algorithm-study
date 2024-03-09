n = int(input())

a = n
for _ in range(n):
  word = input()
  word_list = []

  for w in word:
    if w not in word_list:
      word_list.append(w)
    elif w in word_list and word_list[-1] != w:
      a -= 1
      break
  
print(a)
