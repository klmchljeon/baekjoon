t = int(input())
for case in range(t):
    x = int(input())
    if x == 0:
        print(1)
        print(2)
        continue
    
    a = 1<<30
    b = a+1
    print(2)
    print(a,b)