filepath = "sinhala.lexc"

Kamaroot = {}
with open(filepath) as fp:  
   for line in fp:
      x=line.strip().split(' ')
      if 'කම' in x[0]:
          if x[0] not in Kamaroot:
              Kamaroot[x[0]] = 0
          
filepath = "hunspell_roots"

with open(filepath) as fp:  
   for line in fp:
      x=line.strip().split(' ')
      if 'කම' in x[0]:
          if x[0] not in Kamaroot:
              Kamaroot[x[0]] = 0

filepath = "rootFile"

with open(filepath) as fp:  
   for line in fp:
      x=line.strip().split(' ')
      if 'කම' in x[0]:
          if x[0] not in Kamaroot:
              Kamaroot[x[0]] = 0
          
filepath = "nounc"

with open(filepath) as fp:  
   for line in fp:
      x=line.strip().split(' ')
      for i in x:
          if 'කම' in i:
              if i not in Kamaroot:
                  word = "XXX"+i
                  Kamaroot[word] = 0
          
f = open('KaMaWords', 'w')
for x in Kamaroot:
  f.write(x+"\n")
f.close()
