zero = [1,0]
one = [0,1]
t=int(input())
for case in range(t):
    n=int(input())
    L = len(zero)
    if n>=L:
        for i in range(L,n+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print(zero[n],one[n])