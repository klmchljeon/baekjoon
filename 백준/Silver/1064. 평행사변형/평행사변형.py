def dist(p,q):
    return (p[0]-q[0])**2 + (p[1]-q[1])**2

x1,y1,x2,y2,x3,y3 = map(int,input().split())
a = (x1,y1)
b = (x2,y2)
c = (x3,y3)

lst = [dist(a,b),dist(b,c),dist(c,a)]
lst.sort()
if (lst[2]-(lst[0]+lst[1]))**2 == 4*lst[0]*lst[1]:
    print(-1)
    exit()

for i in range(3):
    lst[i] = lst[i]**0.5

min_ = 2*(lst[0]+lst[1])
max_ = 2*(lst[1]+lst[2])
print(max_-min_)