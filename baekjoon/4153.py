while True : 
  a, b, c = map(int, input().split())
  if a == 0 and b == 0 and c == 0 : 
    break
  if (c > a and c > b) :
    if c**2 == a**2 + b**2 :
      print("right")
    else :
      print("wrong")
  elif (b > a and b > c) :
    if b**2 == a**2 + c**2 :
      print("right")
    else :
      print("wrong")
  else :
    if a**2 == b**2 + c**2 :
      print("right")
    else :
      print("wrong")