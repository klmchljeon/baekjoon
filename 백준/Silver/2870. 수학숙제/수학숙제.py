n = int(input())
lst = []
for _ in range(n):
    st = input()

    tmp = ''
    for i in st:
        if '0' <= i <= '9':
            tmp += i

        elif tmp:
            lst.append(int(tmp))
            tmp = ''

    if tmp:
        lst.append(int(tmp))

lst.sort()
print(*lst,sep='\n')