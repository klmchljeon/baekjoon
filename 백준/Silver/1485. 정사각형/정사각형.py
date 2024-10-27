def dist(a,b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

t = int(input())
for case in range(t):
    lst = []
    for _ in range(4):
        x,y = map(int,input().split())
        lst.append((x,y))

    p = lst[0]
    lst.sort(key = lambda x:dist(p,x))
    lst[2],lst[3] = lst[3],lst[2]

    d = dist(lst[0],lst[1])
    for i in range(4):
        a = dist(lst[i],lst[(i-1)%4])
        b = dist(lst[i],lst[(i+1)%4])
        c = dist(lst[i],lst[(i+2)%4])
        if not (a==b and 2*b==c):
            print(0)
            break
    
    else:
        print(1)