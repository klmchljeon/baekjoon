def s(n,r,c):
    global result
    if n==0:
        return
    else:
        dr,mr = divmod(r,2**(n-1))
        dc,mc = divmod(c,2**(n-1))
        result += int(str(dr)+str(dc),2) * 4**(n-1)
        s(n-1,mr,mc)
        return

n,r,c = map(int,input().split())
result = 0
s(n,r,c)
print(result)