def cal(st):
    n = len(st)
    for i in range(1,n+1):
        if n%i != 0: continue

        p = st[:i]
        for j in range(i,n,i):
            q = st[j:j+i]
            if p != q:
                break

        else:
            return p

s = input()
t = input()
res = cal(s) == cal(t)
print(int(res))