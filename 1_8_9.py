import math
nm=input().split()
n=int(nm[0])
m=int(nm[1])
x=n*m
y=int(math.sqrt(x))
if(x==y**2):
    print('yes')
else:
    print('no')
