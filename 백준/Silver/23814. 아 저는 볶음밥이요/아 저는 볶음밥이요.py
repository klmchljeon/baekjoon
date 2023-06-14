#아 저는 볶음밥이요
d = int(input())
n,m,k = map(int,input().split())

tmp = sorted([d-n%d,d-m%d])

cnt = 0
if k%d >= tmp[0]:
    k -= tmp[0]
    cnt += 1 

if k%d >= tmp[1]:
    k -= tmp[1]
    cnt += 1

if not cnt:
    t = d + k%d
    if k>=t and sum(tmp)<=t:
        k -= sum(tmp)

print(k)