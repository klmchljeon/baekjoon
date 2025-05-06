lst1 = 'abdegopqr@'
lst2 = 'B'
lst3 = 'EGr'
st = input()
cnt = 0
for i in st:
    cnt += i.lower() in lst1
    cnt += i in lst2
    cnt -= i in lst3

print(cnt)