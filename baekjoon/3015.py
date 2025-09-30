import sys
input = sys.stdin.readline

N = int(input())
stack = []  # [(높이, 개수)]
res = 0

for _ in range(N):
  person = int(input())
  
  if not stack or person < stack[-1][0]: # 더 작으면
    stack.append([person, 1])
  
  elif person == stack[-1][0]:  # 같으면
    res += stack[-1][1] # 같은 거만큼 추가
    stack[-1][1] += 1
  
  else: # 더 크면
    while stack and person > stack[-1][0]:  # 작은 애 다 빼기
      res += stack.pop()[1]
    
    if stack and person == stack[-1][0]:  # 같은 거만큼 추가
      res += stack[-1][1]
      stack[-1][1] += 1

    else:
      stack.append([person, 1])
  
  if len(stack) > 1:
    res += 1

print(res)