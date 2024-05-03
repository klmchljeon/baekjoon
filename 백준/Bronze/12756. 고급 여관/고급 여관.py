a = list(map(int,input().split()))
b = list(map(int,input().split()))
while True:
    a[1] -= b[0]
    b[1] -= a[0]

    if a[1]<=0 or b[1]<=0:
        break

if a[1]<=0 and b[1]<=0:
    print('DRAW')
elif a[1]<=0:
    print('PLAYER B')
else:
    print('PLAYER A')