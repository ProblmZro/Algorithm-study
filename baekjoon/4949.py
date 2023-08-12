while True :
  sen = input()
  if sen == "." : break
  lst = []
  for i in sen:
    if i == "(" or i == "[":
      lst.append(i)
    elif i == ")":
      if len(lst) != 0 and lst[-1] == "(": 
        lst.pop(-1)
      else : lst.append(i)
    elif i == "]":
      if len(lst) != 0 and lst[-1] == "[": 
        lst.pop(-1)
      else : lst.append(i)
  if len(lst) == 0 : print("yes")
  else : print("no")
  