n,m = map(int,input().split())
st = input()

dic = dict()
for i in st:
    if not i in dic:
        dic[i] = 0

    dic[i] += 1

p = sorted(dic)
for i in p:
    if m >= dic[i]:
        m -= dic[i]
        dic[i] = 0
    
    else:
        dic[i] -= m
        m = 0
        break

res = []
for i in st[::-1]:
    if dic[i]:
        dic[i] -= 1
        res.append(i)

print(''.join(res[::-1]))