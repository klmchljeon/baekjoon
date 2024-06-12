n = int(input())
st = list(input())

dic = dict()
for i in range(n):
    if not st[i] in dic:
        dic[st[i]] = 0

    dic[st[i]] += 1

res = ''
cnt = 0
for i in dic:
    if cnt < dic[i]:
        cnt = dic[i]
        res = i

print(res,cnt)