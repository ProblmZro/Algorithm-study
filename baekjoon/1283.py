shortcut = []
for _ in range(int(input())):
  Flag = False
  word = input()
  word_list = word.split(" ")
  for i in range(len(word_list)):
    if word_list[i][0].upper() not in shortcut:
      shortcut.append(word_list[i][0].upper())
      word_list[i] = "[" + word_list[i][0] + "]" + word_list[i][1:]
      Flag = True
      break
  if not Flag:
    for i in range(len(word_list)):
      for j in range(len(word_list[i])):
        if word_list[i][j].upper() not in shortcut:
          shortcut.append(word_list[i][j].upper())
          word_list[i] = word_list[i][:j] + '[' + word_list[i][j] + ']' + word_list[i][j+1:]
          Flag = True
          break
      if Flag:
        break
  print(' '.join(word_list))