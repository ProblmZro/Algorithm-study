def Cantorian(array, start, num) : 
  if num // 3 == 0 : return
  for i in range(start + (num // 3), start + (num // 3)*2):
    array[i] = ' '
  Cantorian(array, start, num // 3)
  Cantorian(array, start + (num // 3) * 2 ,num // 3)
while True:
  try:
    n = int(input())
    array = ["-" for _ in range(3**n)]
    Cantorian(array, 0, 3**n)
    ans = ''.join(array)
    print(ans)
  except EOFError:
    break