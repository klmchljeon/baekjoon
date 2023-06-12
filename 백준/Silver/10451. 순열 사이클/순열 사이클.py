#순열 사이클
t = int(input())
for case in range(t):
    n = int(input())
    d = [0] + list(map(int,input().split()))

    cnt = 0
    visit = [False]*(n+1)
    for i in range(1,n+1):
        if not visit[i]:
            visit[i] = True
            cnt += 1

            tmp = d[i]
            while not visit[tmp]:
                visit[tmp] = True
                tmp = d[tmp]

    print(cnt)