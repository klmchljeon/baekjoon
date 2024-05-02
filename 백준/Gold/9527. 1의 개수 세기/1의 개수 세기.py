f = lambda x:(1<<(x-1))*x + 1 if x else 1

def cal(num):
    res = 0
    i = 60
    cnt = 0
    while i >= 0:
        if num&(1<<i) == (1<<i):
            res += f(i)
            res += cnt*(1<<i)
            cnt += 1
        i -= 1

    return res

a,b = map(int,input().split())
print(cal(b)-cal(a-1))