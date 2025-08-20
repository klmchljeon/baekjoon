import sys
input = sys.stdin.read
lst = input().split('\n')

dic = dict()
cnt = 0
for st in lst:
    if not st: continue
    
    if not st in dic:
        dic[st] = 0

    dic[st] += 1
    cnt += 1

for key in dic:
    dic[key] = f'{100*dic[key]/cnt:0.4f}'

p = list(dic.items())
p.sort()
for i in p:
    print(*i)