word = input()

al_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for al in al_list:
  word = word.replace(al, "*")

print(len(word))