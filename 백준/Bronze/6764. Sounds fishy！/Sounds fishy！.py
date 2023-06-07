a,b,c,d = [int(input()) for _ in range(4)]
if a<b and b<c and c<d:
    print('Fish Rising')
elif a>b and b>c and c>d:
    print('Fish Diving')
elif a==b and b==c and c==d:
    print('Fish At Constant Depth')
else:
    print('No Fish')