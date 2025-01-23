st = input()
if 'x' in st:
    if st[-1] == 'x':
        a_ = int(st[:-1])//2
        if a_ == 1:
            a = 'xx'
        elif a_ == -1:
            a = '-xx'
        else:
            a = f'{a_}xx'
        b = ''

    else:
        a_,b = map(int,st.split('x'))
        a_ = a_//2
        if a_ == 1:
            a = 'xx'
        elif a_ == -1:
            a = '-xx'
        else:
            a = f'{a_}xx'

        if b == 1:
            b = '+x'
        elif b == -1:
            b = '-x'
        elif b > 0:
            b = f'+{b}x'
        else:
            b = f'{b}x'

else:
    a = ''
    b = int(st)
    if b == 0:
        print('W')
        exit()
    elif b == 1:
        b = 'x'
    elif b == -1:
        b = '-x'
    else:
        b = f'{b}x'

print(f'{a}{b}+W')