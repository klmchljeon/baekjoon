t = int(input())
for case in range(t):
    n,*d = map(int,input().split())
    cnt = 0
    for i in range(n-1):
        for j in range(i+1,n):
            cnt += d[i]>d[j]

    print(f'Scenario #{case+1}:\n{cnt}\n')