a = '1234567891011'
s = input()
for i in range(1,len(a)+1):
    if s == a[:i]:
        print(i)
        break

else:
    print(-1)