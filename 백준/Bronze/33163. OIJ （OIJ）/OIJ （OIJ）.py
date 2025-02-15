n = int(input())
st = input()
res = ''
for i in st:
    if i == 'J':
        res += 'O'
    elif i == 'O':
        res += 'I'
    else:
        res += 'J'

print(res)