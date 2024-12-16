lst1 = ['social', 'history', 'language', 'literacy']
lst2 = ['bigdata', 'public', 'society']

st = input().split()
for i in st:
    if i in lst1:
        print('digital humanities')
        break

    if i in lst2:
        print('public bigdata')
        break