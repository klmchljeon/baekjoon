t = int(input())
for case in range(t):
    n,s,d = map(int,input().split())

    res = 0
    for _ in range(n):
        di,v = map(int,input().split())
        if s*d >= di:
            res += v

    print(f'Data Set {case+1}:')
    print(res)
    print()