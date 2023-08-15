A, B, C = map(int, input().split())

def DAC(A, B, C):
  if B == 1 :
    return A % C
  if B % 2 == 0 :
    # 10^6 = (10^3)^2
    return DAC(A, B//2, C) ** 2 % C
  else :
    # 10^5 = (10^2)^2 * 10
    return (DAC(A, B//2, C) ** 2) * A % C

print(DAC(A, B, C))