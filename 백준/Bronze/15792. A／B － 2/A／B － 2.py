import decimal
D = decimal.Decimal
decimal.getcontext().prec = 1001
a,b = map(D,input().split())
print(a/b)