#A/B - 2
import decimal
D = decimal.Decimal
decimal.Context(prec = 1001)
a,b = map(D,input().split())
print(a/b)