slst = [100,75,60,50,45,40,36,32,29,26,24,22,20,18,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]

n = int(input())
lst = []
for i in range(n):
    s,p,f,o = map(int,input().split())
    lst.append((s,p,f,o,i))

lst.sort(key = lambda x:(-x[0],x[1],x[2]))

res = [-1]*n

prev = lst[0][:3]
rank = 0
tmp = [lst[0][3:]]
for i in range(1,n):
    if lst[i][:3] == prev:
        tmp.append(lst[i][3:])

    else:
        a = 0
        b = len(tmp)
        for _ in range(b):
            a += slst[rank]
            rank = min(rank+1,30)

        score = a//b + bool(a%b)
        for o,idx in tmp:
            res[idx] = score + o

        prev = lst[i][:3]
        rank = min(i,30)
        tmp = [lst[i][3:]]

if tmp:
    a = 0
    b = len(tmp)
    for _ in range(b):
        a += slst[rank]
        rank = min(rank+1,30)

    score = a//b + bool(a%b)
    for o,idx in tmp:
        res[idx] = score + o

    prev = lst[i][:3]
    rank = min(i,30)
    tmp = [lst[i][3:]]
    
print(*res,sep='\n')