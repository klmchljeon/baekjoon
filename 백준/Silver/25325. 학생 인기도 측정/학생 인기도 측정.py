n = int(input())
lst = input().split()
dic = dict(zip(lst,[0]*len(lst)))
for _ in range(n):
    tmp = input().split()
    for i in tmp:
        dic[i] += 1

p = sorted(dic.items(),key = lambda x:(-x[1],x[0]))
for i in p:
    print(*i)