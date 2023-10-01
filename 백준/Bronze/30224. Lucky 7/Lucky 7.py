st = input()
n = int(st)

res = 0
res += ('7' in st)<<1
res += (n%7==0)
print(res)