nm=input().split()
n=int(nm[0])
m=int(nm[1])
if(n<m):
    min1=n
    max1=m
else:
    min1=m
    max1=n
while(max1%min1!=0):
    x=min1
    min1=max1%min1
    max1=x
print(min1)
