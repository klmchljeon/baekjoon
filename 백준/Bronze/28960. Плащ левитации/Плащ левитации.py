h,l,a,b = map(int,input().split())
case1 = h*2 >= a and l >= b
case2 = h*2 >= b and l >= a
print('YES' if case1 or case2 else 'NO')