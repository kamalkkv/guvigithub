n=int(input())
f=0
x=n//2
for i in range(x,1,-1):
    if(n%i==0):
        f=1
        break
if(f==1):
    print('no')
else:
    print('yes')
