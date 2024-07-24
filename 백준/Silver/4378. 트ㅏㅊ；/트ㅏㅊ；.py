def find(c):
    for i in lst:
        for idx in range(len(i)):
            if i[idx] == c:
                res.append(i[idx-1])
                return 
            
    res.append(' ')
    return

lst = ['`1234567890-=',
       'QWERTYUIOP[]\\',
       'ASDFGHJKL;\'',
       'ZXCVBNM,./']

while True:
    try:
        st = input()
    except:
        break
    res = []
    for i in st:
        find(i)

    print(*res, sep='')