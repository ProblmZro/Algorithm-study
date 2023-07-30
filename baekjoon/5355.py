case = int(input())

for i in range(case) :
  a = list(input().split())
  num = float(a[0])
  op = str(a[1:])

  for j in op : 
    if j == '@' :
      num *= 3
    elif j == '%' :
      num += 5
    elif j == '#' :
      num -= 7
  
  print("%0.2f"%num)
