#두 수의 곱
max_ = 2000000
a,b,c = map(int,input().split())

res = max_*3
for x in range(1,max_):
    for y in range(1,max_):
        if x*y > max_:
            break

        tmp = abs(a-x) + abs(b-y) + abs(c-x*y)
        res = min(res,tmp)

print(res)