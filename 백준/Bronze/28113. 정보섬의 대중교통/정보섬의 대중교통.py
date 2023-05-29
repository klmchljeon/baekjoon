n,a,b = map(int,input().split())
if a < max(n,b):
    print('Bus')
elif a > max(n,b):
    print('Subway')
else:
    print('Anything')