filepath = "sinhala.lexc"

RaNaroot = {}
with open(filepath) as fp:  
   for line in fp:
      x=line.strip().split(' ')
      if 'රණ' in x[0]:
          if x[0] not in RaNaroot:
              RaNaroot[x[0]] = 0
          
filepath = "hunspell_roots"

with open(filepath) as fp:  
   for line in fp:
      x=line.strip().split(' ')
      if 'රණ' in x[0]:
          if x[0] not in RaNaroot:
              RaNaroot[x[0]] = 0

filepath = "rootFile"

with open(filepath) as fp:  
   for line in fp:
      x=line.strip().split(' ')
      if 'රණ' in x[0]:
          if x[0] not in RaNaroot:
              RaNaroot[x[0]] = 0
          
filepath = "nounc"

with open(filepath) as fp:  
   for line in fp:
      x=line.strip().split(' ')
      for i in x:
          if 'රණ' in i:
              if i not in RaNaroot:
                  word = "XXX"+i
                  RaNaroot[word] = 0
          
f = open('RaNaWords', 'w')
for x in RaNaroot:
  f.write(x+"\n")
f.close()
