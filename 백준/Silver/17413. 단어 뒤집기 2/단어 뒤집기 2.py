#단어 뒤집기 2
st = input()

res = []
tmp = []
for i in st:
    if i == '>':
        tmp.append('>')
        res.append(''.join(tmp))
        tmp = []
        continue

    if i == '<':
        a = ''.join(tmp).split()
        for j in range(len(a)):
            a[j] = a[j][::-1]

        res.append(' '.join(a))
        tmp = []

    tmp += i

a = ''.join(tmp).split()
for j in range(len(a)):
    a[j] = a[j][::-1]

res.append(' '.join(a))

print(''.join(res))