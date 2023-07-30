s = str(input())
count = 0

for i in range(0, len(s) // 2) :
  if s[i] == s[len(s)-(i+1)] : count += 1
  else : 
    break

if count == len(s) // 2 or len(s) == 1 : print(1)
else : print(0)