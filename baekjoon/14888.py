N = int(input())
num = list(map(int, input().split()))
opers = list(map(int, input().split()))
res_arr = []

def Back(idx, res):
  if idx == N:
    res_arr.append(res)
    return
  
  if opers[0] > 0:
    opers[0] -= 1
    Back(idx+1, res + num[idx])
    opers[0] += 1
  if opers[1] > 0:
    opers[1] -= 1
    Back(idx+1, res - num[idx])
    opers[1] += 1
  if opers[2] > 0:
    opers[2] -= 1
    Back(idx+1, res * num[idx])
    opers[2] += 1
  if opers[3] > 0:
    opers[3] -= 1
    Back(idx+1, int(res / num[idx]))
    opers[3] += 1

Back(1, num[0])

print(max(res_arr))
print(min(res_arr))