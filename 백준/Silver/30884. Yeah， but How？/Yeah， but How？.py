st = input()
prev = None
res = []
for i in st:
    if prev == '(' and i == ')':
        res.append('1')
    
    if prev == ')' and i == '(':
        res.append('+')

    res.append(i)
    prev = i

print(''.join(res))