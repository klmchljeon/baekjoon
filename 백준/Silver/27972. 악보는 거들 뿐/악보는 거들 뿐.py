#악보는 거들뿐
n = int(input())
d = list(map(int,input().split()))

res = 1
tmp = [None,1]
for i in range(1,n):
    if d[i-1] < d[i]:
        if tmp[0] != False:
            tmp[1] += 1

        else:
            tmp[1] = 2

        tmp[0] = True

    elif d[i-1] > d[i]:
        if tmp[0] != True:
            tmp[1] += 1
        
        else:
            tmp[1] = 2

        tmp[0] = False

    res = max(res,tmp[1])

print(res)