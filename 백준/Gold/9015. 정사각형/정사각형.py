import sys
input = sys.stdin.readline

def translation(a,b):
    return (a[0]+b[0],a[1]+b[1])

def check(a,b):
    d = (a[0]-b[0],a[1]-b[1])

    for i in ((-d[1],d[0]),(d[1],-d[0])):
        if translation(a,i) in st and translation(b,i) in st:
            return True

    return False

def dist(a,b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

t = int(input())
for case in range(t):
    n = int(input())
    lst = []
    for _ in range(n):
        x,y = map(int,input().split())
        lst.append((x,y))

    st = set(lst)
    
    res = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if check(lst[i],lst[j]):
                res = max(res,dist(lst[i],lst[j]))

    print(res)