#캠핑
tc = 1
while True:
    l,p,v = map(int,input().split())
    if not v: break

    res = l*(v//p) + min(l,v%p)
    print(f'Case {tc}: {res}')

    tc += 1