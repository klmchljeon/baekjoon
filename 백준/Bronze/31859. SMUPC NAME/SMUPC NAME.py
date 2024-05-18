n,s = input().split()
n = int(n)

st = ''
cnt = 0
for i in s:
    if not i in st:
        st += i

    else:
        cnt += 1

st += str(cnt+4)
st = str(1906+n) + st
st = 'smupc_' + st[::-1]

print(st)