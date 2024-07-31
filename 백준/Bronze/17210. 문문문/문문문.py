n = int(input())
p = int(input())
if n > 5:
    print("Love is open door")

else:
    for i in range(1,n):
        p ^= 1
        print(p)