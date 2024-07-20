def comp(a, b):
    tmp = 1
    idx = 0
    while True:
        if idx >= n+1 and idx >= m+1:
            return 0
        
        if idx >= n+1:
            return tmp
        
        if idx >= m+1:
            return -tmp
        
        a0 = a[idx]
        b0 = b[idx]
        if a0 < b0:
            return -tmp
        
        if a0 > b0:
            return tmp
        
        tmp = -tmp
        idx += 1

n,*lst1 = map(int,input().split())
m,*lst2 = map(int,input().split())

res = comp(lst1, lst2)
if res == -1:
    print('<')
elif res == 0:
    print('=')
else:
    print('>')
