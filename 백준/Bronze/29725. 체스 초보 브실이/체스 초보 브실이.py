st = 'kpnbrq'
score = '013359'
score = list(map(int,score))

dic = dict()
dic['.'] = 0
for i in range(6):
    dic[st[i]] = -score[i]
    dic[st[i].upper()] = score[i]

res = 0
for i in range(8):
    tmp = input()
    for j in tmp:
        res += dic[j]

print(res)