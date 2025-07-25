def cal(a,b):
    cost = a*10
    if cost >= 5000:
        cost -= 500

    return b*10 / cost

st = 'SNU'
m = -1
res = ''
for i in range(3):
    a,b = map(int,input().split())
    if m < cal(a,b):
        m = cal(a,b)
        res = st[i]

print(res)