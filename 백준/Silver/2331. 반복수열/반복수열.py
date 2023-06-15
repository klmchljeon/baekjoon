#반복수열
a,p = map(int,input().split())

dic = {a:0}
d = [a]
prev = a
while True:
    cur = 0
    for i in map(int,str(prev)):
        cur += i**p

    if cur in dic:
        break
    
    dic[cur] = len(d)
    d.append(cur)

    prev = cur 

print(dic[cur])