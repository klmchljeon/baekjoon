st = list(input())

while st:
    if ''.join(st[-2:]) == 'pi':
        del st[-2:]

    elif ''.join(st[-2:]) == 'ka':
        del st[-2:]
    
    elif ''.join(st[-3:]) == 'chu':
        del st[-3:]

    else:
        print('NO')
        break

else:
    print('YES')