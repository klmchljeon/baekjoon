t = int(input())
for case in range(t):
    n = int(input())
    
    even = (n - n//2)
    k = (n-1)//3
    odd = (n//2 + n%2) - (k//2 + k%2)

    print(even + odd)