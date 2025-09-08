k = int(input())
for case in range(k):
    n = int(input())
    st = input()
    for i in st:
        if i == 'c':
            n += 1
        else:
            n -= 1
    
    print(f'Data Set {case+1}:')
    print(n)
    print()