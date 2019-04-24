filepath ="si_LK.dic.txt"

word = []

with open(filepath) as fp:  
   for line in fp:
      x=line.strip().split('/')
      if x[0] not in word:
          word.append(x[0])


filepath ="rootFile"

root = []

with open(filepath) as fp:  
   for line in fp:
      x=line.strip().split(' : ')
      if x[0] not in root:
          root.append(x[0])
intersection_root =[] 
for x in root:
    if x in word:
        intersection_root.append(x)

print(len(intersection_root))
print(len(word))
print(len(root))
f = open('intersection_root', 'w')
for x in intersection_root:
  f.write(x+"\n")
f.close()
        
f = open('hunspell_roots', 'w')
for x in word:
  f.write(x+"\n")
f.close()
