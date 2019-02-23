nm=input().split()
n=int(nm[0])
m=int(nm[1])
if(n<m):
    min1=n
    max1=m
else:
    max1=n
    min1=m
m=max1
while(max1%min1!=0):
    max1=max1+m
print(max1)
    
