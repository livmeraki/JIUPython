sentence = "The quick brown fox jumps over the lazy dog"
splited = sentence.split()
for i in splited:
    print(i[0].upper()+i[1:], end=' ')
