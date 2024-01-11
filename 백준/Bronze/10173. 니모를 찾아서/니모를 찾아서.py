while True:
    st = input()
    if st == 'EOI':
        break

    if 'nemo' in st.lower():
        print('Found')
    else:
        print('Missing')