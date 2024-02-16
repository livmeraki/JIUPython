"""
Read File and Confirm Contents: CountFile Function
Write a function CountFile(filename) that reads a text file and returns the number of words, the number of characters (excluding spaces), the number of characters (including spaces), and the number of lines. Call the created function, save the results to "output.txt," and then read the file again to print its content.
Instructions:
Use the try ~ except statement when opening the file.
When counting characters, do not include the newline character '\n', regardless of whether spaces are included.
Create the input file named 'input.txt' before starting.
Do not submit the input and output files.
Example "input.txt":
write a function that reads in a text file and prints and
prints the total number of words,
number of letters excluding spaces,
number of letters including spaces,
and the number of lines found in the file.

Content of "output.txt":
Word count: 37
Character count (excluding spaces): 170
Character count (including spaces): 202
Line count: 5
"""

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
        print('error~')
 
CountFile("input.txt")
