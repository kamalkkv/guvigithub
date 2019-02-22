n=int(input())
l=[]
while(n!=0):
    x=n%10
    if(x%2!=0):
        l.append(x)
    n=n//10
for i in range(len(l)-1,-1,-1):
    print(l[i],end=' ')
