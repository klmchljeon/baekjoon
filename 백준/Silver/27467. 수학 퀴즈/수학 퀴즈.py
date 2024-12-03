n = int(input())
lst = list(map(int,input().split()))

p,q = 0,0
for i in lst:
    if i%3 == 0:
        q += 1

    elif i%3 == 1:
        p += 1

    else:
        p -= 1
        q -= 1 

print(p,q)