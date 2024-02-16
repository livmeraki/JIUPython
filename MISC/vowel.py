user_input = input("Input one alphabet: ").lower()
vowel = ['a', 'e', 'i', 'o', 'u']

if(len(user_input)>1):
    print("Wrong entry. Please input one alphabet.")
elif user_input in vowel:
    print("This is a vowel.")
else:
    print("This is a constanant.")
