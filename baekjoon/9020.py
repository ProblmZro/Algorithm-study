def isPrime(max_num) :
  prime_list = [True] * (max_num + 1)
  prime_list[0] = prime_list[1] = False
  for i in range(2, int(max_num**(1/2)) + 1):
    if prime_list[i]:
      for j in range(i**2, max_num + 1, i):
        prime_list[j] = False
  return prime_list

max_num = 1000000
prime_list = isPrime(max_num)

while True:
  n = int(input())
  
  isWrong = True
  if n == 0: break
  for i in range(2, n//2 + 1):
    if prime_list[i]:
      if prime_list[n-i]:
        print(n, "=", i, "+", n-i)
        isWrong = False
        break
  if isWrong:
    print("Goldbach's conjecture is wrong.")