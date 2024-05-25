n = int(input())
a = input().split()
b = input().split()

a = ''.join(a)
b = ''.join(b)

a,b = map(int,(a,b))
print(min(a,b))