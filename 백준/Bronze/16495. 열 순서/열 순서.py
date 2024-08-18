alpha = [chr(i + ord('A')) for i in range(26)]
dic = dict(zip(alpha,range(1,27)))

st = input()

st = st[::-1]
res = 0

for i in range(len(st)):
    res += dic[st[i]]*(26**i)

print(res)