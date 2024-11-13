t = int(input())
for case in range(t):
    n,p,q = map(int,input().split())
    lst = list(map(int,input().split()))
    lst.sort()

    cnt = 0
    for i in range(min(p,n)):
        if q >= lst[i]:
            q -= lst[i]
            cnt += 1
        else:
            break

    print(f'Case {case+1}: {cnt}')