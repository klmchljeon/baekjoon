#곱셈

a,b,c = map(int,input().split())

def fpow(C, n, p):
	if n == 1:
		return C
	else:
		x = fpow(C, n//2, p)
		if n % 2 == 0:
			return ((x%p)*(x%p))%p
		else:
			return ((((x%p)*(x%p))%p)*C%p)%p

result = fpow(a,b,c)%c
print(result)