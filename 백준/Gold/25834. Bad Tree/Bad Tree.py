n,k = map(int,input().split())
s,e = 1,n

m = 2**(n-1)
if m < k:
    print(-1)
    exit()

lst = []
while m:
    m = m//2
    if k <= m:
        lst.append(s)
        s += 1

    else:
        lst.append(e)
        e -= 1
        k -= m

print(*lst)