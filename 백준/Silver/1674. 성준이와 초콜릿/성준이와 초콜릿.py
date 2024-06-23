import sys
max_ = 1000000

tmp = sys.stdin.readlines()

qlst = []
clst = []
for i in tmp:
    q,*order = i.split()
    if q == 'Query':
        qlst.append(int(order[0]))
    else:
        a,b = order
        c = q == 'Coffee'
        clst.append((int(a),float(b),c))

qlst.sort()

f = [lambda n,t:8*n-t/12, lambda n,t:2*n-(t**2)/79]

res = [0.0]*(max_+1)
for t,n,tp in clst:
    cnt = 0
    while True:
        p = f[tp](n,cnt)
        if p <= 0 or t+cnt > max_:
            break

        res[t+cnt] += p
        cnt += 1

for t in qlst:
    r = max(1.0, round(res[t],1))
    print(t,r)