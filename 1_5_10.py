import math
n=int(input())
if(math.ceil(math.log(n,2))==math.floor(math.log(n,2))):
    print('yes')
else:
    print('no')
