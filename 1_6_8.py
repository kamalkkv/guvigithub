nk=input().split()
n=int(nk[0])
k=int(nk[1])
l=[]
x=0
for i in range(0,n):
    x=int(input())
    l.append(x)
if(l.count(k)>0):
    print('yes')
else:
    print('no')
