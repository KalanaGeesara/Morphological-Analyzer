filepath = "sinhala.lexc"

root = {}
with open(filepath) as fp:  
   for line in fp:
      x=line.strip().split(' ')
      root[x[0]] = 0

filepath ="nounc"

a={}
not_found = []
with open(filepath) as fp:  
   for line in fp:
      x=line.strip().split(' ')
      for i in x:
          build =''
          found = 0
          for j in i:
              build+=j
              if build in root:
                  if build not in a:
                      a[build] = 0
                      found = 1
                  else:
                      a[build]+=1
                      found = 1
          if found == 0:
              if build not in not_found:
                  not_found.append(build)

print(len(not_found))
print(len(a))
print(len(root))
f = open('not_found', 'w')
for x in not_found:
  f.write(x+"\n")
f.close()
f = open('rootFile', 'w')
for x in a:
  f.write(x+" : "+str(a[x])+"\n")
f.close()
