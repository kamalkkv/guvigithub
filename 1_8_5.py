s=input()
l=len(s)
l1=list(s)
x=l//2
if(l%2==0):
    l1[x]='*'
    l1[x-1]='*'
else:
    l1[x]='*'
print(''.join(map(str,l1)))
    
