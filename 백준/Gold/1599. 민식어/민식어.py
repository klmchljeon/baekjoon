def f(st):
    res = []
    i = 0
    while i < len(st):
        if st[i:i+2] == 'ng':
            res.append(dic['ng'])
            i += 1
        else:
            res.append(dic[st[i]])

        i += 1

    return res

alpha = 'a b k d e g h i l m n ng o p r s t u w y'.split()

dic = dict(zip(alpha,range(len(alpha))))

n = int(input())
d = [input() for _ in range(n)]
d.sort(key = f)

print(*d,sep='\n')