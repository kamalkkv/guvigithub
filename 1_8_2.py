v=['a','e','i','o','u']
s=input()
f=1
for i in v:
    if(i in s):
        print('yes')
        f=0
        break
if(f!=0):
    print('no')

