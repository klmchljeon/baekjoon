st = input()

cnt = 0
for i in st:
    cnt += i in 'aeiou'

cnt2 = cnt + st.count('y')
print(cnt,cnt2)