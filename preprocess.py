import random
filepath ="sinhala.lexc"

arr =[]

with open(filepath) as fp:  
   for line in fp:
      x=line.strip().split(';')
      if len(x)>1:
          arr.append(x[0]+";")
      else:
          arr.append(x[0])

f = open('workfile3', 'w')
for x in arr:
  f.write(x+"\n")
f.close()
