lst1 = ['social', 'history', 'language', 'literacy']
lst2 = ['bigdata', 'public', 'society']

st = input()
for i in lst1:
    if i in st:
        print('digital humanities')
        exit()

for i in lst2:
    if i in st:
        print('public bigdata')
        exit()