n=int(input())
a=n//2
f=1
for i in range(2,a+1):
    if(n%i==0):
        f=0
        break
if(f==0):
    print('no')
else:
    print('yes')
