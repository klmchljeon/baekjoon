p,r = map(int,input().split())
if 10*p < 2*r:
    print('weak')
elif 10*p < 4*r:
    print('normal')
elif 10*p < 6*r:
    print('strong')
else:
    print('very strong')