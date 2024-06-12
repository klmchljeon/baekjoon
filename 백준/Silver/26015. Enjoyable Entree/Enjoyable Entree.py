n = int(input())

if n > 50:
    print(100/3, 200/3)

else:
    b = -200/3*((-1/2)**(n-1) - 1)
    a = 100-b
    print(a,b)