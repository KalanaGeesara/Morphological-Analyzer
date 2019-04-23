import random
filepath ="tagged.txt"

tags = ['JJ', 'NNJ', 'NNC', 'POST', 'VP', 'AUX', 'CC', 'RP', 'VNF', 'CM', 'VFM', 'FS', 'NNP', 'DET', 'NIP', 'NCV', 'RB', 'VNN', 'PRP', 'PCV', 'JCV', 'UNK', 'NVB', 'QUE', 'ABB', 'NDT', 'QBE']

words =[]
for i in range(len(tags)):
   words.append([tags[i]])

a={}
with open(filepath) as fp:  
   for line in fp:
      x=line.strip().split(' ')
      if (len(x)==2):
         if x[1] not in a:
            a[x[1]] = 0
         else:
            a[x[1]] +=1
         if (x[1]!='PUNC' and x[1]!='NUM'):
            words[tags.index(x[1])].append(x[0])
word_count =[]
for i in words:
   word_count.append({})
   for j in i:
      if j not in word_count[-1]:
         word_count[-1][j] = 0
      else:
         word_count[-1][j]+=1

top_words= []
for i in word_count:
   w= sorted(i.items(), key = 
                lambda kv:(kv[1], kv[0]))
   q=w[-10:]
   for i in q:
      top_words.append(i[0])
print(top_words)  
b=[]
sum = 0
for i in a:
   b.append(a[i])
   sum+=a[i]
b.sort(reverse=True)
print(sum)
z=[]
for i in b:
   for j in a:
      if a[j] == i:
         z.append(j)

word_num =[]
for i in b:
   word_num.append(round(i*1000/sum))
print(word_num)
new_word_list = top_words
for i in range(len(z)):
   if (z[i]!='PUNC' and z[i]!='NUM'):
      list_word = words[tags.index(z[i])]
      k=0
      att=0
      while((k<word_num[i]) and (att<3*word_num[i])):
         ran_word = list_word[random.randint(1,b[i])]
         if(ran_word not in new_word_list):
            new_word_list.append(ran_word)
            k+=1
         att+=1
print(new_word_list)
                           
                           
f = open('workfile3', 'w')
for x in new_word_list:
  f.write(x+" ")
f.close()
