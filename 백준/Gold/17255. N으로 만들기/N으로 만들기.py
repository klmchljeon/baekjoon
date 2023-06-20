#N으로 만들기 45:34
def cal(idx,m):
    s,e = idx,idx
    res = [d[idx]]
    for i in m:
        if i:
            s -= 1
            res.append(d[s]+res[-1])

        else:
            e += 1
            res.append(res[-1]+d[e])

    return tuple(res)

def dfs(l):
    if len(s) == n-1:
        tmp.append(s[:])
        return 
    
    for i in (0,1):
        if l-i==-1: continue
        if len(s)+l==n-1 and not i: continue
        
        s.append(i)
        dfs(l-i)
        s.pop()

d = list(input())
n = len(d)

lst = []
s = []
for i in range(n):
    tmp = []
    dfs(i)
    lst.append(tmp)

st = set()
for i in range(n):
    for j in lst[i]:
        st.add(cal(i,j))

print(len(st))