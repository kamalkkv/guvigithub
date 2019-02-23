while(True):
    s=input()
    if(len(s)==0):
        break
    l=list(s)
    s1=set(l)
    if(len(l)-len(s1)!=0):
        print('no')
    else:
        print('yes')
        
