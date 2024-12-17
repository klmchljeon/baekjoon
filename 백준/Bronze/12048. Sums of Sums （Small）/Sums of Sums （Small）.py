t = int(input())
for case in range(t):
    n,q = map(int,input().split())
    p = list(map(int,input().split()))

    lst = []
    for i in range(n):
        for j in range(i,n):
            lst.append(sum(p[i:j+1]))

    lst.sort()
    
    print(f'Case #{case+1}:')
    for _ in range(q):
        l,r = map(int,input().split())
        print(sum(lst[l-1:r]))