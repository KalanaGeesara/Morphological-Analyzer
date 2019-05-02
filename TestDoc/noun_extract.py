filepath ="tagged.txt"

nnj={}
nnc={}
allw={}
j=0
c=0
tot=0
total={}
with open(filepath) as fp:  
   for line in fp:
      x=line.strip().split(' ')
      if x[0] not in allw:
          allw[x[0]] =0
          tot+=1
      if (len(x)==2):

 
          if x[1] == 'NNP':
              if x[0] not in total:
                  nnj[x[0]] = 0
                  total[x[0]] = 0
                  j+=1
          if x[1] == 'NNC':
              if x[0] not in total:
                  nnc[x[0]] = 0
                  total[x[0]] = 0
                  c+=1


           
                  
print(j/tot,c/tot)
inter= 0
for x in nnc:
    if x in nnj:
        inter+=1
print(inter)
    
f = open('nounp', 'w')
for x in nnj:
  f.write(x+" ")
f.close()

f = open('nounc', 'w')
for x in nnc:
  f.write(x+" ")
f.close()
