import re
n=int(input())
list1=[]
lst=[]

for i in range(0,n):
    s1=input()
    if s1:
     list1.append(s1)
    
for j in list1:
    se=re.findall(r'[\w\.]+@[\w\.]+',j)

    for k in se:
        if k[-1]==".":
            k=k[0:-1]
        if k not in lst:
    
            lst.append(k)
    
                
lst.sort()
print (';'.join(str(x) for x in lst))