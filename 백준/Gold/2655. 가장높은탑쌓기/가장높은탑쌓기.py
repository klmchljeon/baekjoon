n = int(input())
lst = []
for i in range(n):
    a,h,w = map(int,input().split())
    lst.append((a,h,w,i+1))

lst.sort(key = lambda x:x[0])

dp = [(0,None)]*(n+1)
for i in range(n):
    tmp = [0,None]
    for j in range(i):
        if lst[j][2] < lst[i][2]:
            if tmp[0] < dp[j+1][0]:
                tmp = [dp[j+1][0],j+1]

    dp[i+1] = [tmp[0]+lst[i][1],tmp[1]]

m = [0,None]
s = None
for i in range(1,n+1):
    if m[0] < dp[i][0]:
        m = dp[i]
        s = i

idx = m[1]
res = [lst[s-1][3]]
while idx != None:
    res.append(lst[idx-1][3])
    idx = dp[idx][1]

print(len(res))
print(*res[::-1],sep='\n')