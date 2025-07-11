n,m = map(int,input().split())
for case in range(m):
    lst = list(map(int,input().split()))
    lst.sort()

    p = []
    while lst and lst[-1] > 0:
        p.append(lst.pop())

    cnt = 0
    while lst and lst[-1] == 0:
        cnt += 1
        lst.pop()

    m = lst[:]
    
    a = 1
    for i in p:
        a *= i

    b = 1
    for i in range(0,len(m)-1,2):
        b *= m[i]*m[i+1]

    if len(p)>0 or len(m)>=2:
        print(a*b)
    else:
        if cnt:
            print(0)
        else:
            print(m[0])