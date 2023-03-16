while True:
    n,*d = map(int,input().split())
    if not n: break
        
    res = []
    prev = None
    for i in d:
        if i != prev:
            res.append(i)
        prev = i
        
    res.append('$')
    print(*res)