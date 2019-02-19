l=input().split()
s1=l[0]
s2=l[1]
c1=0
c2=0
for i in range(0,len(s1)):
    if(ord(s1[i])>=ord(s2[i])):
        c1=c1+1
    else:
        c2=c2+1
if(c1>=c2):
    print(s1)
else:
    print(s2)
    
        
