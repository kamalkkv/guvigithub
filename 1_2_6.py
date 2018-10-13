n=int(input())
q=int(input())
for j in range(n+1,q):
    a=j//2
    f=1
    if(j==1):
        continue
    else:
        for i in range(2,a+1):
            if(j%i==0):
                f=0
                break
        if(f!=0):
            print(j,end=' ')
