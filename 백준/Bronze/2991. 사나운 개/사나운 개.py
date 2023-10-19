max_ = 1000

a,b,c,d = map(int,input().split())
p,m,n = map(int,input().split())

lst = [0]*(2*max_)
for x,y in (a,b),(c,d):
    idx = 0
    while idx < max_:
        for i in range(idx,idx+x):
            lst[i] += 1

        idx += x+y

for i in p,m,n:
    print(lst[i-1])