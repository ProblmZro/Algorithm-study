max = 246912

prime_list = [0] * 2 + [1] * max
for i in range(2, int(max**(1/2))+1):
  if prime_list[i] == 1:
    for j in range(2*i, max+1, i):
      prime_list[j] = 0

while True :
  n = int(input())
  if n == 0 : break  
  print(sum(prime_list[n+1:2*n+1]))