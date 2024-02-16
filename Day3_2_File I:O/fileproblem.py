#문제 1

def CountFile(filename):
    try:
        f = open(filename,'r')
        count1 = 0 # 단어 수
        count2 = 0 # 문자 수(공백제외)
        count3 = 0 # 문자 수(공백포함)
        count4 = 0 # 줄수
        lines = f.readlines()
        for i in lines:
            count4 += 1
            for ch in i:
                if ch != '\n':
                    count3 += 1
                if not ch.isspace():
                    count2 += 1
                if ch == ' ':
                    count1 += 1
        print(count1+count4)
        print(count2)
        print(count3)
        print(count4)
        f.close()
    except:
        print('Oh no error :((')

CountFile("input.txt")
