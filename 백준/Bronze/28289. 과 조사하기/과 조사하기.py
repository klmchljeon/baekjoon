p = int(input())
lst = [0]*4
for _ in range(p):
    g,c,n = map(int,input().split())
    if g == 1:
        lst[3] += 1

    elif c <= 2:
        lst[0] += 1

    else:
        lst[c-2] += 1

print(*lst,sep='\n')