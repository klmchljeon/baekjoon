#나3곱2
f = lambda x:(-x[2],x[1])

n = int(input())
d = list(map(int,input().split()))

lst = []
for i in range(n):
    x = d[i]
    tmp = [d[i],0,0]
    while True:
        if x%2==0:
            x//=2
            tmp[1] += 1
        elif x%3==0:
            x//=3
            tmp[2] += 1
        else:
            break

    lst.append(tuple(tmp))

lst.sort(key = f)

res = [i for i,*_ in lst]
print(*res)