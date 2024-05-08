max_ = 16

def dfs():
    m = len(s)
    if m == 2*n:
        print(*s)
        exit()

    tmp = []
    for i in range(m):
        if cnt[s[i]] == 1 and m-i == s[i]+1:
            tmp.append(s[i])

    if len(tmp) >= 2:
        return 
    
    if len(tmp) == 1:
        x = tmp[0]
        cnt[x] += 1
        s.append(x)
        dfs()
        s.pop()
        cnt[x] -= 1
        return 
    
    for i in range(n):
        if cnt[lst[i]] == 0:
            cnt[lst[i]] += 1
            s.append(lst[i])
            dfs()
            s.pop()
            cnt[lst[i]] -= 1

n = int(input())
lst = list(map(int,input().split()))
lst.sort()

s = []
cnt = [0]*(max_+1)
dfs()
print(-1)