n = int(input())
st = input()

cntr = 0
cntb = 0
prev = None
for i in st:
    if prev != i and i == 'R':
        cntr += 1

    if prev != i and i == 'B':
        cntb += 1

    prev = i

print(min(cntb,cntr) + 1)