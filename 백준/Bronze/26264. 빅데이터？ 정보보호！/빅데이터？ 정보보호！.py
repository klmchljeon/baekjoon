n = int(input())
st = input()
idx = 0
cnt = 0
while idx < len(st):
    if st[idx] == 's':
        idx += 8
        cnt += 1
    else:
        idx += 7

if 2*cnt < n:
    print('bigdata?')
elif 2*cnt > n:
    print('security!')
else:
    print('bigdata? security!')