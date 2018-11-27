t=int(input())
if(t<60):
    print('0 ',t)
else:
    t1=t//60
    t=t-t1*60
    print(t1,' ',t)
