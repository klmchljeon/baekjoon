n,m = map(int,input().split())
num,*d = map(int,input().split())
p = set(d)

lst = []
for _ in range(m):
    a,*b = map(int,input().split())
    lst.append(set(b))

for _ in range(m):
    for party in lst:
        for i in party:
            if i in p:
                p.update(party)
                break

res = 0
for party in lst:
    
    flag = True
    for i in party:
        if i in p:
            flag = False
            break

    res += flag

print(res)