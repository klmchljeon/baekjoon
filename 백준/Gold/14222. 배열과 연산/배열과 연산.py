n,k = map(int,input().split())
d = list(map(int,input().split()))

for i in range(1,n+1):
    if i in d:
        d.remove(i)
        continue

    num = i
    while num > 0:
        num -= k
        if num in d:
            d.remove(num)
            break

    else:
        print(0)
        break

else:
    print(1)