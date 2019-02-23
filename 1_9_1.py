while(True):
    nm=input().split()
    if(len(nm)==0):
        break
    n=int(nm[0])
    m=int(nm[1])
    print(abs(n-m))
