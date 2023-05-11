#2022는 무엇이 특별할까? 
def cal(lst):
    t = 0
    for i in range(d):
        t += lst[i]*(d**i)

    return t

def dfs():
    global ans
    if len(s) == d:
        if s[-1] == 0: return 
        res = cal(s)
        if res > n:
            ans = min(ans, res)

        return 

    for i in range(d):
        if not i in s:
            s.append(i)
            dfs()
            s.pop()

n,d = map(int,input().split())

s = []
ans = 1e9
dfs()
print(ans if ans != 1e9 else -1)