dic = {
    'CU':'see you',
    ':-)':'I’m happy',
    ':-(':'I’m unhappy',
    ';-)':'wink',
    ':-P':'stick out my tongue',
    '(~.~)':'sleepy',
    'TA':'totally awesome',
    'CCC':'Canadian Computing Competition',
    'CUZ':'because',
    'TY':'thank-you',
    'YW':'you’re welcome',
    'TTYL':'talk to you later'

}

while True:
    st = input()
    if st in dic:
        print(dic[st])
    else:
        print(st)

    if st == 'TTYL':
        break