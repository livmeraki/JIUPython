sentence = "The quick brown fox jumps over the lazy dog"
splited = sentence.split()
diff = ord('a')-ord('A')

for word in splited:
    if ord('a')<ord(word[0])<ord('z'):
        print(chr(ord(word[0])-diff)+word[1:], end=' ')
    else:
        print(word, end=' ')
