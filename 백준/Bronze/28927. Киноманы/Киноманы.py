conv = lambda x,y,z:x*3 + y*20 + z*120
a = conv(*map(int,input().split()))
b = conv(*map(int,input().split()))
if a>b:
    print('Max')
elif a<b:
    print('Mel')
else:
    print('Draw')