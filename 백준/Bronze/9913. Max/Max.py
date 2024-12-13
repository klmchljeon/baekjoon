n = int(input())
lst = [0]*(1001)
for i in range(n):
    a = int(input())
    lst[a] += 1

print(max(lst))