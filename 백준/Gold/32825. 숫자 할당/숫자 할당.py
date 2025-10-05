def bt1():
    if len(s) == 6:
        lst.append(tuple(s))
        return

    for i in dd:
        if not i in s:
            s.append(i)
            bt1()
            s.pop()

    return

def bt2():
    if len(dd) == 6:
        bt1()
        return 
    
    for i in range(1,14):
        if not dd or dd[-1] < i:
            dd.append(i)
            bt2()
            dd.pop()

    return 

a,b,c,d,e,f,g,h = map(int,input().split())

s = []
lst = []

dd = []
arr = []

bt2()

def check(k):
    return 1<=k<=13 and num[k]==0

res = 0
for idx in lst:
    num = [0]*14
    for i in idx:
        num[i] = 1

    l_ = h - idx[5]
    #print(l_)
    if not check(l_): continue
    num[l_] = 1

    i_ = g - (idx[3]+idx[4])
    #print(i_)
    if not check(i_): continue
    num[i_] = 1

    e_ = f - (idx[0]+idx[1]+idx[2])
    if not check(e_): continue
    num[e_] = 1

    d_ = d - idx[2]
    if not check(d_): continue
    num[d_] = 1

    c_ = c - (idx[1]+idx[4])
    if not check(c_): continue
    num[c_] = 1

    b_ = b - (idx[0]+idx[3]+idx[5])
    if not check(b_): continue

    a1 = e - (b_ + c_ + d_)
    a2 = a - (e_ + i_ + l_)
    if not (a1 == a2 and check(a1)): continue

    res += 1

print(res)