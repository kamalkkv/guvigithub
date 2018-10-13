n=int(input())
k=int(input())
l=[]
for i in range(0,n):
    x=int(input())
    l.append(x)
sum=0
for i in range(0,k):
    sum=sum+l[i]
print(sum)
