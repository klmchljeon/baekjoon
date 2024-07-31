a,b,c = map(int,input().split())
p = 1
flag = True
for i in (a,b,c):
    if i&1:
        p *= i
        flag = False

if flag:
    print(a*b*c)
else:
    print(p)