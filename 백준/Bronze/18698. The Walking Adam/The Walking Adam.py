n = int(input())
for case in range(n):
    st = input()
    res = 0
    for i in st:
        if i=='U':
            res += 1
        else:
            break
            
    print(res)