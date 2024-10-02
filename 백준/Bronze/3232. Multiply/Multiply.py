def conv(lst,b):
    res = 0
    lst = lst[::-1]
    for i in range(len(lst)):
        res += lst[i]*(b**i)

    return res

f = lambda x:list(map(int,x))

t = int(input())
for case in range(t):
    p,q,r = map(f,input().split())
    
    b = 0
    s = max(*p,*q,*r) + 1
    for i in range(s,17):
        if conv(p,i)*conv(q,i) == conv(r,i):
            b = i
            break

    print(b)