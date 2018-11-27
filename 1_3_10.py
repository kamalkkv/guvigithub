t1=int(input())
m1=int(input())
t2=int(input())
m2=int(input())
t=0
m=0
if(t1<t2):
    if(m1<m2):
        m=60-m1+m2
        t=t2-t1
        m=m%60
        print(t,' ',m)
    if(m1>m2):
        m=60-m1+m2
        t=t2-t1-1
        print(t,' ',m)
    if(m1==m2):
        t=t2-t1
        m=0
        print(t,' ',m)
if(t2<t1):
    if(m2<m1):
        m=60-m2+m1
        t=t1-t2
        #t3=m//60
        #t=t+t3
        m=m%60
        print(t,' ',m)
    if(m2>m1):
        m=60-m2+m1
        t=t1-t2-1
        print(t,' ',m)
    if(m1==m2):
        t=t1-t2
        m=0
        print(t,' ',m)


        
