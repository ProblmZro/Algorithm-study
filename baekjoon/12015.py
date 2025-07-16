N = int(input())
A = list(map(int, input().split()))
res = [A[0]]

def findIdx(a):
  start, end = 0, len(res) - 1

  while start <= end:
    mid = (start+end) // 2
    if res[mid] == a:
      return mid
    elif res[mid] < a:
      start = mid + 1
    else:
      end = mid - 1

  return start
  
for a in A:
  if res[-1] < a:
    res.append(a)
  else:
    idx = findIdx(a)
    res[idx] = a

print(len(res))

# res = []

# 10 20 30 40 50
# 25

# # 6
# # 10 20 10 30 20 50

# # 20 25 10 12 25 30 40

# 20 30 10 50 



# 핵심은, 수열 A를 처음부터 끝까지 for를 돌면서 원소를 이용하여 배열 LIS를 만드는데, 이 리스트 LIS의 원소들은 A의 "가장 긴 증가하는 부분 수열"을 만족하지는 않지만, 이 리스트 LIS의 길이 값 자체만은 A의 "가장 긴 증가하는 부분 수열" 조건을 만족한다는 것을 이해하는 것이다.