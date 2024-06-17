def check(p):
    for i in range(n-1):
        for j in range(i+1,n):
            if intersect(p[i],p[j]):
                return False
            
    return True

def bt():
    if len(s) == n:
        tmp = []
        for i in range(n):
            tmp.append((a[i],b[s[i]]))

        if check(tmp):
            print(*map(lambda x:x+1,s),sep='\n')
            exit()

        return
    
    for i in range(n):
        if not i in s:
            s.append(i)
            bt()
            s.pop()

def ccw(p1,p2,p3):
    x1,y1 = p1
    x2,y2 = p2
    x3,y3 = p3
    return (x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)

def intersect(l1,l2):
    p1,p2 = l1
    p3,p4 = l2

    ccw1 = ccw(p1,p2,p3)*ccw(p1,p2,p4)
    ccw2 = ccw(p3,p4,p1)*ccw(p3,p4,p2)

    if ccw1==0 and ccw2==0:
        if p1>p2: p1,p2 = p2,p1
        if p3>p4: p3,p4 = p4,p3
        return p3<=p2 and p1<=p4

    return ccw1<=0 and ccw2<=0

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
b = [list(map(int,input().split())) for _ in range(n)]

s = []
bt()