n = int(input())
h,d,k = map(int,input().split())
lst = [int(input()) for _ in range(n)]

res = 0
for t in range(-1,n-1):
    for i in range(1<<n):
        tmp = h
        dis = d
        prev = None
        skill = None
        for j in range(n):
            if t==j: 
                skill = 3
            elif i|(1<<j)==i:
                skill = 2
            else:
                skill = 1

            damage = max(0,lst[j]-dis)
            if skill == 1:
                damage //= 2
            
            elif skill == 2:
                dis += k
                damage = max(0,damage-k)

            if prev != 3:
                tmp -= damage
            
            prev = skill

        res = max(res,tmp)

print(res if res else -1)