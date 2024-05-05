n = int(input())
for case in range(n):
    a,b = map(int,input().split('.'))
    c = (a*100 + b)*10

    res = round((c*4//5),-1)//10
    print(f'${res//100}.{res%100:02d}')