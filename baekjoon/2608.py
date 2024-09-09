dic = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
dic2 = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
dic3 = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}

str1 = input()
str2 = input()

def sum_str(strn):
  sum, i = 0, 0
  while i < len(strn):
    if i+1 < len(strn):
      if strn[i:i+2] in dic2:
        sum += dic2[strn[i:i+2]]
        i += 2
        continue
    if strn[i] in dic:
      sum += dic[strn[i]]
      i += 1
  return sum

def str_sum(num):
  res = ''
  while num > 0:
    for k, v in dic3.items():
      while num >= k:
        res += v
        num -= k
  return res

sum_res = sum_str(str1) + sum_str(str2)

print(sum_res)
print(str_sum(sum_res))