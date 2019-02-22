s=input()
l=len(s)
s1=''
for i in range(l-1,-1,-1):
    s1=s1+s[i]
if(s==s1):
    print('yes')
else:
    print('no')
