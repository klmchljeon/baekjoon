n = int(input())
st = list(input())

idx = None
for i in range(n):
    if st[i] == 'O':
        idx = i
        break

k = 0
k += i-1>=0 and st[i-1]=='.'
k += i+1<n and st[i+1]=='.'

if k==0:
    print('yunsu')
    exit()

if k==1:
    print('mingyu')
    exit()

k = 0
k += i-2>=0 and st[i-2]=='.'
k += i+2<n and st[i+2]=='.'

if k==2:
    print('draw')
    exit()

cnt = st.count('.')
res = 'draw' if k else 'yunsu'
print('mingyu' if cnt&1 else res)