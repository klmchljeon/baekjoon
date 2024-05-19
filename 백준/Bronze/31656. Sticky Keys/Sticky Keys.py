st = input()
prev = None
res = ''
for i in st:
    if prev != i:
        res += i

    prev = i

print(res)