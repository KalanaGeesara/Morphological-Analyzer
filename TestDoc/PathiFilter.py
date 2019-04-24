filepath = "sinhala.lexc"

RaNaroot = {}
with open(filepath) as fp:  
   for line in fp:
      x=line.strip().split(' ')
      if 'පති්' in x[0]:
          RaNaroot[x[0]] = 0
          
filepath = "hunspell_roots"

with open(filepath) as fp:  
   for line in fp:
      x=line.strip().split(' ')
      if 'පති' in x[0]:
          RaNaroot[x[0]] = 0

filepath = "rootFile"

with open(filepath) as fp:  
   for line in fp:
      x=line.strip().split(' ')
      if 'පති' in x[0]:
          RaNaroot[x[0]] = 0
          
filepath = "nounc"

with open(filepath) as fp:  
   for line in fp:
      x=line.strip().split(' ')
      for i in x:
          if 'පති' in i:
              word = "XXX"+i
              RaNaroot[word] = 0
          
f = open('PathiWords', 'w')
for x in RaNaroot:
  f.write(x+"\n")
f.close()
