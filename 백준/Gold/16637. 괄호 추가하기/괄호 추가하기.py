#괄호 추가하기 27:41
min_ = -int(1e10)

def cal(a,op,b):
    if op == '+':
        return (a+b,)
    
    if op == '-':
        return (a-b,)
    
    if op == '*':
        return (a*b,)

def sim(order):
    arr = d[:]
    for i in range(n//2-1,-1,-1):
        if not order[i]: continue

        arr[i*2:i*2+3] = cal(*arr[i*2:i*2+3])

    arr = arr[::-1]
    res = arr.pop()
    while arr:
        oper = arr.pop()
        b = arr.pop()
        res = cal(res,oper,b)[0]

    return res

def dfs():
    if len(s) == n//2:
        lst.append(s[:])
        return 
    
    for i in (0,1):
        if s and s[-1] and i: 
            continue

        s.append(i)
        dfs()
        s.pop()

n = int(input())
d = list(input())
for i in range(0,n,2):
    d[i] = int(d[i])

lst = []
s = []
dfs()

res = min_
for i in lst:
    res = max(res,sim(i))

print(res)