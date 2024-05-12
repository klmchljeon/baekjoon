x,m = map(int,input().split())
dic = dict()
dic[x] = 1

res = 0
for _ in range(m+1):
    dic2 = dict()
    for i in dic:
        res += i*dic[i]
        a = i//2
        b = i//2 + i%2
        for x in (a,b):
            if not x in dic2:
                dic2[x] = 0
 
            dic2[x] += dic[i]

    dic = dic2

print(res)