plate = str(input())
height = 10

for i in range(len(plate) - 1) :
  if(plate[i] == plate [i+1]) :
    height += 5
  else :
    height += 10

print(height)