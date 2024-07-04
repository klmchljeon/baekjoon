n = list(map(int,input()))
k = int(input()) - 1

res = []
for i in range(64):
    while n and not n[-1] in (1,2,6,7):
        res.append(n.pop())
        
    if k&(1<<i):
        if n:
            res.append(n[-1] + 5*(n[-1] < 4))
            n.pop()

        else:
            print(-1)
            break

    else:
        if n:
            res.append(n[-1] - 5*(n[-1] > 4))
            n.pop()

else:
    print(''.join(map(str,res[::-1])))