n = int(input())
pa,pb = 0,0
for _ in range(n):
    a,b = map(int,input().split())
    if a < pa or b < pb:
        print('no')
        break

    pa = a
    pb = b

else:
    print('yes')