n = int(input())
st = input()
res = 0
for i in st:
    res += ord(i) - ord('A') + 1

print(res)