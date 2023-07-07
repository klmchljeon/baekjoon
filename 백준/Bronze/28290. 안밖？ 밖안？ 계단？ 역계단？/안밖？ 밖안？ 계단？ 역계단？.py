dic = {'fdsajkl;':'in-out', 'jkl;fdsa':'in-out', 'asdf;lkj':'out-in', ';lkjasdf':'out-in', 'asdfjkl;':'stairs', ';lkjfdsa':'reverse'}

st = input()
if st in dic:
    print(dic[st])
else:
    print('molu')