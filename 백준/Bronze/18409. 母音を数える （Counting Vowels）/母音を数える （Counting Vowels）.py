n = int(input())
st = input()

a = ['a','i','e','o','u']
cnt = 0
for i in st:
    cnt += i in a
    
print(cnt)