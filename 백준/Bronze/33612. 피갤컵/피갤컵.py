n = int(input())
a = 2024
b = 8 + (n-1)*7
a += (b-1)//12
b = (b-1)%12 + 1
print(a,b)