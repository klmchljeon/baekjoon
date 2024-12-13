a,b,c = map(int,input().split())
if a == 0: raise AssertionError

d = b**2 - 4*a*c

if d <= 0:
    print('둘다틀렸근')
    exit()

p = int(d**0.5)
if p**2 != d:
    print('둘다틀렸근')
    exit()

if not ((-b+p)%(2*a) == 0 and (-b-p)%(2*a) == 0):
    print('둘다틀렸근')
    exit()

x1 = (-b+p)//(2*a)
x2 = (-b-p)//(2*a)

k = 1
for x in (x1,x2):
    for i in range(1,20):
        if x == (1<<i):
            break

    else:
        print('정수근')
        exit()

print('이수근')