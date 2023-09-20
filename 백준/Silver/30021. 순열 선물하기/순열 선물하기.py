n = int(input())
if n==2:
    print("NO")
    exit()

res = [1,3,2] + list(range(4,n+1))
print("YES")
print(*res[:n])