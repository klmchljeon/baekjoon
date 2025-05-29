import random
mod = 10001

n = int(input())
lst = [int(input()) for _ in range(n)]
p = list(range(10001))
q = list(range(10001))
random.shuffle(p)
random.shuffle(q)

for a in p:
    for b in q:
        res = []
        tmp = lst[0]
        for i in range(1,n):
            tmp = (a*tmp + b)%mod
            res.append(tmp)

            tmp = (a*tmp + b)%mod
            if tmp != lst[i]:
                break

        else:
            tmp = (a*tmp + b)%mod
            res.append(tmp)
            
            print(*res,sep='\n')
            exit()