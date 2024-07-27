n = int(input())
if n == 0:
    print(0)
    exit()

if n%2 == 0:
    print(-1)
    exit()

print(n.bit_length())