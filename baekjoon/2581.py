arr = ""
def ten_to_k(n, k):
    global arr
    if n == 0:
        return 
    ten_to_k(n//k, k)
    arr+=str(n%k)

def is_prime(n):
    if n<=1:
        return False
    if n == 2 or n == 3:
        return True
    i = 2
    for i in range(2, int(n**(1/2))+1) :
      if(n % i == 0) :
        return False
    return True


def solution(n, k):
    answer = 0
    ten_to_k(n, k)
    arr1 = arr.split('0')
    print(arr1)
    for i in arr1:
        if i != ''and is_prime(int(i)):
            answer += 1
    return answer

arr = '00'

print(arr.split('0'))