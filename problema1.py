with open ('doc.txt','r') as f:
    a=f.readline().split(',')
a.sort()
with open ('doc1.txt','w') as f:
    for i in a:
        f.write(str(i)+'\n')
