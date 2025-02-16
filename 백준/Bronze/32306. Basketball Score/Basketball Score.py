a = list(map(int,input().split()))
b = list(map(int,input().split()))

a_ = sum([a[i]*(i+1) for i in range(3)])
b_ = sum([b[i]*(i+1) for i in range(3)])
if a_ > b_:
    print(1)
elif a_ < b_:
    print(2)
else:
    print(0)