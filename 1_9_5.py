s=input()
o=''
e=''
for i in range(0,len(s)):
    if(i%2==0):
        o=o+s[i]
    else:
        e=e+s[i]
print(o,end=' ')
print(e)
    
