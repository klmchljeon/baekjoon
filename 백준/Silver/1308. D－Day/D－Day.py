import datetime

y1,m1,d1 = map(int,input().split())
y2,m2,d2 = map(int,input().split())

flag = False
if y2-y1>1000:
    flag = True
elif y2-y1==1000 and m2>m1:
    flag = True
elif y2-y1==1000 and m2==m1 and d2>=d1:
    flag = True

if flag:
    print('gg')
    exit()

t1 = datetime.datetime(y1,m1,d1)
t2 = datetime.datetime(y2,m2,d2)
res = (t2-t1).days
print(f'D-{res}')