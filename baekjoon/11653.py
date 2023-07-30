num = int(input())
a = 0

for i in range(2, int(num / 2 + 1)) :
  while(num % i == 0) :
    print(i)
    num //= i
    a += 1

if(a == 0 and num != 1) : 
  print(num)