max_ = int(1e18)

p1,p2,p3,idx = map(int,input().split())

d = (p1,p2,p3)
p = [0,0,0]
for i in range(3):
    tmp = d[i]
    cnt = 0
    while tmp < max_:
        tmp *= d[i]
        cnt += 1

    p[i] = cnt

lst = []
for i in range(p[0]):
    for j in range(p[1]):
        for k in range(p[2]):
            tmp = (d[0]**i) * (d[1]**j) * (d[2]**k)
            if tmp > max_:
                break

            lst.append(tmp)

lst.sort()
print(lst[idx])