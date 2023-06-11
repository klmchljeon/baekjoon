#2048 (Easy)

def dfs(lst,cnt):
    global res
    if cnt == 5:
        for i in lst:
            for j in i:
                res = max(res,j)

        return 
    
    nlst = [[0]*n for _ in range(n)]
    for i in range(n):
        tmp = []
        for j in range(n):
            if lst[i][j]:
                if tmp and tmp[-1] == [lst[i][j],0]:
                    tmp[-1][0] *= 2
                    tmp[-1][1] = 1

                else:
                    tmp.append([lst[i][j],0])

        for j in range(len(tmp)):
            nlst[i][j] = tmp[j][0]

    dfs(nlst,cnt+1)

    nlst = [[0]*n for _ in range(n)]
    for i in range(n):
        tmp = []
        for j in range(n-1,-1,-1):
            if lst[i][j]:
                if tmp and tmp[-1] == [lst[i][j],0]:
                    tmp[-1][0] *= 2
                    tmp[-1][1] = 1

                else:
                    tmp.append([lst[i][j],0])

        for j in range(len(tmp)):
            nlst[i][n-j-1] = tmp[j][0]

    dfs(nlst,cnt+1)

    nlst = [[0]*n for _ in range(n)]
    for j in range(n):
        tmp = []
        for i in range(n):
            if lst[i][j]:
                if tmp and tmp[-1] == [lst[i][j],0]:
                    tmp[-1][0] *= 2
                    tmp[-1][1] = 1

                else:
                    tmp.append([lst[i][j],0])

        for i in range(len(tmp)):
            nlst[i][j] = tmp[i][0]

    dfs(nlst,cnt+1)

    nlst = [[0]*n for _ in range(n)]
    for j in range(n):
        tmp = []
        for i in range(n-1,-1,-1):
            if lst[i][j]:
                if tmp and tmp[-1] == [lst[i][j],0]:
                    tmp[-1][0] *= 2
                    tmp[-1][1] = 1

                else:
                    tmp.append([lst[i][j],0])

        for i in range(len(tmp)):
            nlst[n-i-1][j] = tmp[i][0]

    dfs(nlst,cnt+1)

n = int(input())
d = [list(map(int,input().split())) for _ in range(n)]

res = 0
dfs(d,0)

print(res)