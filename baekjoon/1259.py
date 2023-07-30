while True :
  num = input()
  if num == "0" : break

  isTrue = 0
  for i in range(len(num) // 2) :
    if num[i] != num[len(num) - i - 1] :
      print("no")
      isTrue += 1
      break
  
  if(isTrue == 0) : print("yes")