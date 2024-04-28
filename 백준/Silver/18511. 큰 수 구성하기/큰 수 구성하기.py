def check(lst):
    l = 0
    res = 0
    for i in range(len(lst)-1,-1,-1):
        res += lst[i]*(10**l)
        l += 1

    if res <= n:
        return res
    else:
        return None

def bt(p):
    if len(s) == p:
        tmp = check(s)
        if tmp != None:
            print(tmp)
            exit()
        return 
    
    for i in d:
        s.append(i)
        bt(p)
        s.pop()

n,k = map(int,input().split())
m = len(str(n))

d = list(map(int,input().split()))
d.sort(reverse = True)

s = []
for i in range(m,0,-1):
    bt(i)