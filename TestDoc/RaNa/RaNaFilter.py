def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

##filepath = "sinhala.lexc"
##
##RaNaroot = {}
##with open(filepath) as fp:  
##   for line in fp:
##      x=line.strip().split(' ')
##      if 'රණ' in x[0]:
##          if x[0] not in RaNaroot:
##              RaNaroot[x[0]] = 0
##          
##filepath = "hunspell_roots"
##
##with open(filepath) as fp:  
##   for line in fp:
##      x=line.strip().split(' ')
##      if 'රණ' in x[0]:
##          if x[0] not in RaNaroot:
##              RaNaroot[x[0]] = 0
##
##filepath = "rootFile"
##
##with open(filepath) as fp:  
##   for line in fp:
##      x=line.strip().split(' ')
##      if 'රණ' in x[0]:
##          if x[0] not in RaNaroot:
##              RaNaroot[x[0]] = 0
##          
##filepath = "nounc"
##
##with open(filepath) as fp:  
##   for line in fp:
##      x=line.strip().split(' ')
##      for i in x:
##          if 'රණ' in i:
##              if i not in RaNaroot:
##                  word = "XXX"+i
##                  RaNaroot[word] = 0
##          
##f = open('RaNaWords', 'w')
##for x in RaNaroot:
##  f.write(x+"\n")
##f.close()
#######################################
##filepath = "RaNaWords"
##
##RaNaroot = {}
##with open(filepath) as fp:  
##   for line in fp:
##      x=line.strip().split(' ')
##      if len(x)==2 and x[1]=='1':
##          if x[0] not in RaNaroot:
##             if x[0][-1]=='ය':
##                word = x[0][:len(x[0])-1]
##                RaNaroot[word] = 0
##             else:
##                RaNaroot[x[0]] = 0
##f = open('RaNaWords_Final', 'w')
##for x in RaNaroot:
##  f.write(x+"\n")
##f.close()
#######################################

filepath = "RaNaWords"

RaNawords = []
with open(filepath) as fp:  
   for line in fp:
      x=line.strip().split(' ')
      if x[0][0]=='X':
         word = x[0][3:]
         RaNawords.append(word.strip())
f =0
for i in RaNawords:
   if i =='ජනාධිපතිවරණයේ්':
      f+=1
print(f)
filepath = "Inflection"

inflections = ['']
with open(filepath) as fp:  
   for line in fp:
      x=line.strip().split(' ')
      inflections.append(x[0])


filepath = "RaNaWords_Final"

RaNa_Generated = []
with open(filepath) as fp:  
   for line in fp:
      x=line.strip().split(' ')
      for i in inflections:
         RaNa_Generated.append(x[0]+i)


p=0
for i in RaNa_Generated:
   if i in RaNawords:
      RaNawords = remove_values_from_list(RaNawords, i)
      #RaNawords.append("XXX"+i)
      p+=1

filepath = "RaNaWords_Final"

with open(filepath) as fp:  
   for line in fp:
      x=line.strip().split(' ')
      for i in RaNawords:
         if x[0] in i:
            RaNawords = remove_values_from_list(RaNawords, i)

         
f = open('test1', 'w')
for x in RaNawords:
  f.write(x+"\n")
f.close()
f = open('test2', 'w')
for x in RaNa_Generated:
  f.write(x+"\n")
f.close()
print(len(RaNawords))     
print(len(RaNa_Generated))
print(p)
