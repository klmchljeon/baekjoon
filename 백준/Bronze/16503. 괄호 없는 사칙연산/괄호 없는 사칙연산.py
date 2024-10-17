def cal(a,b,oper):
    if oper == '+':
        return a+b
    
    if oper == '-':
        return a-b
    
    if oper == '*':
        return a*b
    
    tmp = abs(a)//abs(b)
    if a*b > 0:
        return tmp
    else:
        return -tmp

k1,o1,k2,o2,k3 = input().split()
k1,k2,k3 = map(int,(k1,k2,k3))

a = cal(cal(k1,k2,o1),k3,o2)
b = cal(k1,cal(k2,k3,o2),o1)
print(*sorted((a,b)),sep='\n')