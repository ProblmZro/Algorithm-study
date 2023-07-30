num = int(input())
string = input()
sum = 0
M = 1234567891

for i in range(len(string)) :
  sum += (ord(string[i]) - 96) * (31 ** i) 

print(sum % M)