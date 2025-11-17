n = int(input())
if n >= 1000000:
    b = n * 20 // 100
    a = n - b

elif n >= 500000:
    b = n * 15 // 100
    a = n - b

elif n >= 100000:
    b = n * 10 // 100
    a = n - b

else:
    b = n * 5 // 100
    a = n - b

print(b,a)