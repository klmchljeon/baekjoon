cnt = 1
while True:
    st = input()
    if st == '0': break
    r,w,l = map(int,st.split())

    flag = w**2 + l**2 <= (r*2)**2
    if flag:
        print(f"Pizza {cnt} fits on the table.")
    else:
        print(f"Pizza {cnt} does not fit on the table.")

    cnt += 1
