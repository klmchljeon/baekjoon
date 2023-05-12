a,d,k = map(int,input().split())
tmp = k-a

if tmp%d or tmp*d<0:
    print('X')
else:
    print(tmp//d+1)