text = input('enter text u want:')# python is my fav
words = text.split()
print(words)
print('-'*50)
cnt = 0
for word in words:
    print(word,'---->')
    cnt += 1
    count = 0
    for ch in word:
        print(ch)
        count += 1
    else:
        print('number of char in {} is {}'.format(word, count))
else:
    print('number of words in {} is {}'.format(text, cnt))

