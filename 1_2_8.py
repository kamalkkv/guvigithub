n=int(input())
q=int(input())
for i in range(n+1,q):
    x=str(i)
    l=len(x)
    sum=0
    d=0
    while(i!=0):
        d=i%10
        i=i//10
        sum=sum+d**l
    i=int(x)
    if(sum==i):
        print(i)
