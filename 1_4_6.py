s=input()
c=0
for i in s:
    if(i.isalnum()):
        continue
    elif(i.isspace()):
        continue
    else:
        c+=1
print(c)
