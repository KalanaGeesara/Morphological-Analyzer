##filepath = "sinhala.lexc"
##s=['ggg']
##print(s[0][-1])
RaNaroot = {}
##with open(filepath) as fp:  
##   for line in fp:
##      x=line.strip().split(' ')
##      if  len(x[0])>2 and x[0][-1] =='ම':
##          if x[0] not in RaNaroot:
##              RaNaroot[x[0]] = 0
##          
##filepath = "hunspell_roots"
##
##with open(filepath) as fp:  
##   for line in fp:
##      x=line.strip().split(' ')
##      if len(x[0])>2 and x[0][-1] =='ම':
##          if x[0] not in RaNaroot:
##              RaNaroot[x[0]] = 0

filepath = "rootFile"

with open(filepath) as fp:  
   for line in fp:
      x=line.strip().split(' ')
      if len(x[0])>2 and x[0][-1] =='ම':
          if x[0] not in RaNaroot:
              RaNaroot[x[0]] = 0
          
filepath = "nounc"

with open(filepath) as fp:  
   for line in fp:
      x=line.strip().split(' ')
      for i in x:
          if len(i)>2 and i[-1] =='ම':
              if i not in RaNaroot:
                  word = "XXX"+i
                  RaNaroot[word] = 0
          
f = open('MaWords', 'w')
for x in RaNaroot:
  f.write(x+"\n")
f.close()
