st = list(input())
p = list('UAPC')
res = ''
for i in p:
    if not i in st:
        res += i

print(res)