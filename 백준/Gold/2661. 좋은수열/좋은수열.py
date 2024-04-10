def check(num):
    cnt = 1
    m = len(s)
    while cnt*2 <= m+1:
        a = s[m-2*cnt+1:m-cnt+1]
        b = s[m-cnt+1:] + [num]
        if a == b:
            return False
        
        cnt += 1
        
    return True

def dfs():
    if len(s) == n:
        print(*s,sep='')
        exit()

    for i in range(1,4):
        if check(i):
            s.append(i)
            dfs()
            s.pop()

n = int(input())
s = []
dfs()