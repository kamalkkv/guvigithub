n=int(input())
l=[]
for i in range(n):
    a=int(input())
    l.append(a)
l.sort()
if(n%2==0):
    i=int(n/2-1)
    j=i+1
    print((l[i]+l[j])//2)
else:
    i=int((n+1)/2-1)
    print(l[i])
