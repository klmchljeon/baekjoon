def odd(length):
    c = n//length
    res = [c]
    for i in range(1,length//2+1):
        res.append(c-i)
        res.append(c+i)

    if sum(res)==n and min(res)>=0:
        return sorted(res)
    else:
        return None

def even(length):
    c = n//length
    res = [c,c+1]
    for i in range(1,length//2):
        res.append(c-i)
        res.append(c+1+i)

    if sum(res)==n and min(res)>=0:
        return sorted(res)
    else:
        return None

n,l = map(int,input().split())

for i in range(l,101):
    if i&1:
        tmp = odd(i)
    else:
        tmp = even(i)

    if tmp != None:
        print(*tmp)
        break

else:
    print(-1)