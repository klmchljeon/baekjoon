num = set(range(1,10001))
der_num = set()

def d(n):
    der = n
    for i in str(n):
        der += int(i)
    der_num.add(der)

for i in range(1,10000):
    d(i)

self_num = sorted(num-der_num)
for i in self_num:
    print(i)