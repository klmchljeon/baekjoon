st = input()

lst = []
flag = False
tmp = ''
for i in st:
    if i in '.?':
        lst.append(tmp + i)
        tmp = ''
        flag = False

    elif 'A' <= i <= 'Z':
        tmp = i
        flag = True

    elif flag:
        tmp += i

for i in lst:
    if i[:7] != 'What is': continue
    if i[-1] != '?': continue

    print('Forty-two' + i[4:-1] + '.')