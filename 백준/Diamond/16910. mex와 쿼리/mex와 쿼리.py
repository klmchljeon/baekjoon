#mex와 쿼리
import sys
input = sys.stdin.readline

def propagate(s,e):
    val = lazy[s//sqn]
    lazy[s//sqn] = None

    if val == 1:
        pro_t(s,e)
    elif val == 0:
        pro_f(s,e)
    elif val == -1:
        pro_x(s,e)

    return 

def pro_t(s,e):
    for i in range(s,e):
        lst[i] = True

def pro_f(s,e):
    for i in range(s,e):
        lst[i] = False

def pro_x(s,e):
    for i in range(s,e):
        lst[i] ^= True

def cal_seg(s,e):
    res = [None]*2
    for i in range(s,e):
        if lst[i]:
            if res[0] == None:
                res[0] = i

        else:
            if res[1] == None:
                res[1] = i

    return res

def update_t(l,r):
    left = l%sqn and l<=r
    if left:
        s = (l//sqn)*sqn
        e = min(n,s+sqn)
        propagate(s,e)

    while l%sqn and l<=r:
        lst[l] = True
        l += 1

    if left:
        minb[s//sqn],mexb[s//sqn] = cal_seg(s,e)

    right = (r+1)%sqn and l<=r
    if right:
        s = (r//sqn)*sqn
        e = min(n,s+sqn)
        propagate(s,e)

    while (r+1)%sqn and l<=r:
        lst[r] = True
        r -= 1

    if right:
        minb[s//sqn],mexb[s//sqn] = cal_seg(s,e)
        
    while l<=r:
        lazy[l//sqn] = True
        minb[l//sqn] = l
        mexb[l//sqn] = None
        l += sqn

    return

def update_f(l,r):
    left = l%sqn and l<=r
    if left:
        s = (l//sqn)*sqn
        e = min(n,s+sqn)
        propagate(s,e)

    while l%sqn and l<=r:
        lst[l] = False
        l += 1

    if left:
        minb[s//sqn],mexb[s//sqn] = cal_seg(s,e)

    right = (r+1)%sqn and l<=r
    if right:
        s = (r//sqn)*sqn
        e = min(n,s+sqn)
        propagate(s,e)

    while (r+1)%sqn and l<=r:
        lst[r] = False
        r -= 1

    if right:
        minb[s//sqn],mexb[s//sqn] = cal_seg(s,e)

    while l<=r:
        lazy[l//sqn] = False
        minb[l//sqn] = None
        mexb[l//sqn] = l
        l += sqn

    return 

def update_x(l,r):
    left = l%sqn and l<=r
    if left:
        s = (l//sqn)*sqn
        e = min(n,s+sqn)
        propagate(s,e)

    while l%sqn and l<=r:
        lst[l] ^= True
        l += 1

    if left:
        minb[s//sqn],mexb[s//sqn] = cal_seg(s,e)

    right = (r+1)%sqn and l<=r
    if right:
        s = (r//sqn)*sqn
        e = min(n,s+sqn)
        propagate(s,e)

    while (r+1)%sqn and l<=r:
        lst[r] ^= True
        r -= 1

    if right:
        minb[s//sqn],mexb[s//sqn] = cal_seg(s,e)

    while l<=r:
        if lazy[l//sqn] == -1:
            lazy[l//sqn] = None
        elif lazy[l//sqn] == None:
            lazy[l//sqn] = -1
        else:
            lazy[l//sqn] ^= True

        minb[l//sqn],mexb[l//sqn] = mexb[l//sqn],minb[l//sqn]
        l += sqn

    return 

def cal():
    for i in mexb:
        if i != None:
            return idx[i]

n = int(input())
nums = set()
query = []
for _ in range(n):
    q,l,r = map(int,input().split())
    nums.add(l)
    nums.add(r)

    query.append((q,l,r))

tmp = sorted(nums)
idx = []
if tmp[0] != 1: idx.append(1)

for i in tmp:
    if idx and idx[-1]+1 != i:
        idx.append(idx[-1]+1)
    
    idx.append(i)

idx.append(idx[-1]+1)

n = len(idx)
dic = dict(zip(idx,range(n)))
sqn = int(n**0.5)+1

del tmp,nums

lst = [False]*n
minb = [None]*sqn
mexb = [i*sqn for i in range(sqn)]

lazy = [None]*sqn
for q,a,b in query:
    l = dic[a]
    r = dic[b]
    if q==1: 
        update_t(l,r)

    elif q==2: 
        update_f(l,r)

    else: 
        update_x(l,r)

    print(cal())