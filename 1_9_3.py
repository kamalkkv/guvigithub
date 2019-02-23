while(True):
    s=input()
    if(len(s)==0):
        break
    if('%' in s):
        i=s.index('%')
    if('/' in s):
        i=s.index('/')
    s1=s[0:i]
    s2=s[i+1:]
    x=int(s1)
    y=int(s2)
    if(s[i]=='%'):
        print(x%y)
    if(s[i]=='/'):
        print(x//y)
    
        
