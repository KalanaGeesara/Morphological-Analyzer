filepath = "sinhala.lexc"

RaNaroot = {}
with open(filepath) as fp:  
   for line in fp:
      x=line.strip().split(' ')
      if 'රණ' in x[0]:
          RaNaroot[x[0]] = 0
          
filepath = "hunspell_roots"

with open(filepath) as fp:  
   for line in fp:
      x=line.strip().split(' ')
      if 'රණ' in x[0]:
          RaNaroot[x[0]] = 0

filepath = "rootFile"

with open(filepath) as fp:  
   for line in fp:
      x=line.strip().split(' ')
      if 'රණ' in x[0]:
          RaNaroot[x[0]] = 0
          
f = open('RaNAWords', 'w')
for x in RaNaroot:
  f.write(x+"\n")
f.close()
