#카이사르 암호
st = input()
res = ''
for i in st:
    res += chr(ord(i) - 3 + 26*(i<='C'))

print(res)