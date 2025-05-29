def bt(depth = 0):
    global tmp
    if depth == 6:
        return 
    
    for i in lst:
        tmp += i * 10**depth
        dp[tmp] = 0
        bt(depth+1)
        tmp -= i * 10**depth

def cal(k):
    if dp[k] != -1:
        return dp[k]
    
    res = 100
    for i in range(2,int(k**0.5)+1):
        if k%i != 0: continue

        a = cal(i)
        b = cal(k//i)
        if a != -1 and b != -1:
            res = min(res,a+b+1)

    dp[k] = res if res!=100 else -1
    return dp[k]

max_ = 1000000

t = int(input())
for case in range(t):
    n,*lst = list(map(int,input().split()))
    dp = [-1]*(max_+1)
    if 1 in lst and 0 in lst:
        dp[max_] = 0

    tmp = 0
    bt()

    m = int(input())
    for _ in range(m):
        k = int(input())
        print(cal(k))