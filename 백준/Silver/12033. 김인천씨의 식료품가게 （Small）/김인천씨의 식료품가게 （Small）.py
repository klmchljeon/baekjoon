t = int(input())
for case in range(t):
    n = int(input())
    lst = list(map(int,input().split()))
    
    res = []
    for i in range(n):
        tmp = lst.pop(0)

        p = tmp*4//3
        for j in range(len(lst)):
            if lst[j] == p:
                lst.pop(j)
                break

        res.append(tmp)

    print(f'Case #{case+1}:',*res)