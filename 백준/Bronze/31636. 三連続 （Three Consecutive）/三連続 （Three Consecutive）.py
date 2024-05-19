n = int(input())
st = input()
for i in range(n-2):
    if st[i:i+3] == 'ooo':
        print('Yes')
        break
else:
    print('No')