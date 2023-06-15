#전북대학교
n = int(input())
if n%2==0:
    print('I LOVE CBNU')
    exit()

print('*'*n)
for i in range(n//2+1):
    c = n//2
    st = [' ']*n
    st[c+i:] = ('*',)
    st[c-i] = '*'
    print(''.join(st))