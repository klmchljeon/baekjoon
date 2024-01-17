#제곱근

n = int(input())

def bisection(a,b):
    while a<b:
        m = (a+b)//2
        pow_m = m**2
        if pow_m == n:
            return m
        if pow_m > n:
            b = m
        else:
            a = m
    return (a+b)//2
result = bisection(1,n)
print(result)